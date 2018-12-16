from pytest import fixture, mark

from django.contrib.auth.models import User
from django.test import Client
from django.urls import reverse

from lead.models import Contact


# #############################################################################
# ##     Data for parametrize
# #############################################################################
# URL & corresponding templates for an authenticated user with no contact
AUTH_WITHOUT_CONTACT = [
    ('lead:index', {}, 200, [
        'lead/contact_list.html', 'base.html', 'lead/none.html'
    ]),
    ('lead:view', {'contact_id': 1}, 404, ['404.html', 'base.html']),
    ('lead:edit', {'contact_id': 1}, 404, ['404.html', 'base.html']),
    ('lead:add', {}, 200, [
        'lead/contact_form.html', 'lead/contact_list.html', 'base.html'
    ]),
]

# URL & corresponding templates for an anonymous user
ANONYMOUS = [
    ('lead:add', {}, []),
    ('lead:index', {}, []),
    ('lead:view', {'contact_id': 1}, []),
    ('lead:edit', {'contact_id': 1}, []),
]


# URL & corresponding templates for an authenticated user with 5 contacts
AUTH_WITH_FIVE_CONTACTS = [
    ('lead:view', ['lead/contact_detail.html', 'lead/contact_list.html', 'base.html']),
    ('lead:edit', ['lead/contact_form.html', 'lead/contact_list.html', 'base.html']),
]


# #############################################################################
# ##     Fixtures
# #############################################################################
@fixture
def sample_user():
    return {'username': 'zoé', 'password': 'zoézoézoé'}


@fixture
def sample_contacts():
    return [
        {'first_name': 'jean', 'last_name': 'bon', 'email': 'jean@b.on'},
        {'first_name': 'lidye', 'last_name': 'oduvillage', 'email': 'li@d.yo'},
        {'first_name': 'paul', 'last_name': 'ochon', 'email': 'paul@auch.on'},
        {'first_name': 'ana', 'last_name': 'liz', 'email': 'an@al.iz'},
        {'first_name': 'cara', 'last_name': 'melmou', 'email': 'cara@melm.ou'},
    ]


@fixture
def client_anon():
    """ Provide a Django test client """
    return Client()


@fixture
def client_auth(sample_user):
    user, created = User.objects.get_or_create(**sample_user)
    client = Client()
    client.force_login(user)

    return client


@fixture
def contact_list(sample_contacts, sample_user):
    user, created = User.objects.get_or_create(**sample_user)

    for c in sample_contacts:
        Contact.objects.create(user=user, **c)

    return Contact.objects.values(
        'id',
        *sample_contacts[0].keys()
    ).all().order_by('-id')


@fixture
def new_contact():
    return {
        'first_name': 'new',
        'last_name': 'user',
        'email': 'new@us.er',
        'role': 'test dummy',
        'role': 'test dummy',
        }


# #############################################################################
#   lead.views.Contact{List,Detail,Create,Add}()
# #############################################################################
@mark.parametrize("url, kwargs, templates", ANONYMOUS)
def test_reach_pages_anonymous(client_anon, url, kwargs, templates):
    response = client_anon.get(reverse(url, kwargs=kwargs))

    assert response.status_code == 302
    assert reverse('login') in response.url
    assert response.templates == templates


@mark.parametrize("url, kwargs, status_c, templates", AUTH_WITHOUT_CONTACT)
@mark.django_db
def test_reach_pages_authenticated_without_contact(
        client_auth, url, kwargs, status_c, templates
):
    response = client_auth.get(reverse(url, kwargs=kwargs))

    assert response.status_code == status_c
    assert [t.name for t in response.templates][:3] == templates


@mark.parametrize("url, templates", AUTH_WITH_FIVE_CONTACTS)
@mark.django_db
def test_reach_pages_authenticated_with_contacts(
        sample_user,
        sample_contacts,
        url,
        templates,
):

    user = sample_user
    user, created = User.objects.get_or_create(**user)
    client = Client()
    client.force_login(user)

    for c in sample_contacts:
        Contact.objects.create(user=user, **c)

    contact = Contact.objects.values(
        'id',
        'user_id',
        *sample_contacts[0].keys()
    ).filter(user=user)[:1]

    response = client.get(reverse(url, args=[
        contact.values_list('id', flat=True).get()
    ]))

    assert response.status_code == 200
    assert [t.name for t in response.templates][:3] == templates

    for label, value in sample_contacts[4].items():
        assert value == response.context['contact'].all()[label]


# #############################################################################
#   lead.views.ContactList()
# #############################################################################
@mark.django_db
def test_reach_contactlist_authenticated_with_contacts(
        client_auth,
        contact_list,
        sample_contacts,
):
    response = client_auth.get(reverse('lead:index'))

    assert response.status_code == 200
    assert [t.name for t in response.templates] == [
        'lead/contact_list.html',
        'base.html',
        'lead/list.html'
    ]


# #############################################################################
#   lead.views.ContactCreate()
# #############################################################################
@mark.django_db
def test_contact_create(client_auth, new_contact):
    response = client_auth.post(reverse('lead:add'), new_contact)

    assert response.status_code == 302
    assert response.url == reverse('lead:index')

# #############################################################################
#   lead.models.__str__()
# #############################################################################
@mark.django_db
def test_contact__str__(client_auth, contact_list, sample_contacts):
    contact = Contact.objects.get(email=sample_contacts[0]['email'])

    assert contact.__str__() == 'jean'


# #############################################################################
#   lead.models.all()
# #############################################################################
@mark.django_db
def test_contact_all(client_auth, contact_list, sample_contacts):
    contact = Contact.objects.get(email=sample_contacts[0]['email'])
    contact_dict = contact.all()

    for label, field in sample_contacts[0].items():
        assert contact_dict[label] == field


# #############################################################################
#   lead.models.get_short_name()
# #############################################################################
@mark.django_db
def test_contact_get_short_name(client_auth, contact_list, sample_contacts):
    contact = Contact.objects.get(email=sample_contacts[1]['email'])

    assert contact.get_short_name() == 'lidye'


# #############################################################################
#   lead.models.get_full_name()
# #############################################################################
@mark.django_db
def test_contact_get_full_name(client_auth, contact_list, sample_contacts):
    contact = Contact.objects.get(email=sample_contacts[2]['email'])

    assert contact.get_full_name() == 'paul ochon'


# #############################################################################
#   lead.models.was_created_today()
# #############################################################################
@mark.django_db
def test_contact_was_created_today(client_auth, contact_list, sample_contacts):
    contact = Contact.objects.get(email=sample_contacts[3]['email'])

    assert contact.was_created_today()
