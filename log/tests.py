from pytest import fixture, mark

from django.contrib.auth.models import User
from django.test import Client
from django.urls import reverse

from lead.models import Contact
from log.models import Entry


# #############################################################################
# ##     Data for parametrize
# #############################################################################
# URL & corresponding templates for an anonymous user
ANONYMOUS = [
    ('lead:log:create', {'contact_id': 1}),
    ('lead:log:detail', {'contact_id': 1, 'entry_id': 1}),
]

# URL & corresponding templates for an authenticated user with no contact
AUTH_WITHOUT_CONTACT = [
    ('lead:log:create', {'contact_id': 1}, 403, ['403.html', 'base.html']),
    ('lead:log:detail', {'contact_id': 1, 'entry_id': 1}, 404, ['404.html', 'base.html']),
]

# #############################################################################
# ##     Fixtures
# #############################################################################
@fixture
def sample_user_zoe():
    return {'username': 'zoé', 'password': 'zoézoézoé'}


@fixture
def client_anon():
    """ Provide a Django test client """
    return Client()


@fixture
def client_auth(sample_user_zoe):
    user, created = User.objects.get_or_create(**sample_user_zoe)
    client = Client()
    client.force_login(user)

    return client


@fixture
def entry_list(sample_contacts, sample_user_zoe, sample_entries):
    user, created = User.objects.get_or_create(**sample_user_zoe)

    contact = Contact.objects.create(user=user, **sample_contacts[2])

    for e in sample_entries:
        Entry.objects.create(user=user, contact=contact, **e)

    return Entry.objects.values(
        'id',
        'user_id',
        'contact_id',
        *sample_entries[0].keys(),
    ).filter(user=user, contact=contact,)[:1]


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
def sample_entries():
    return [
        {'title': 'entrée A', 'desc': "Tu restes pour le lotto-owe ce soir"},
        {'title': 'Entry:2', 'desc': "y'a baeckeoffe ?"},
        {'title': 'Entrée,c', 'desc': "Yeuh non, merci vielmols !"},
        {'title': '4-entry', 'desc': "mais che dois partir à la Coopé…"},
        {'title': 'E-ENTRÉE', 'desc': "de Truchtersheim acheter des mänele."},
    ]


# #############################################################################
#   log.views.{UserCreate|UserDelete|UserDetail|UserUpdate}()
# #############################################################################
@mark.parametrize("url, kwargs", ANONYMOUS)
def test_reach_pages_anonymous(client_anon, url, kwargs):
    response = client_anon.get(
        reverse(url, kwargs=kwargs)
    )

    assert response.status_code == 302
    assert reverse('login') in response.url


# #############################################################################
#   log.views.{UserCreate|UserDelete|UserDetail|UserUpdate}()
# #############################################################################
@mark.parametrize("url, kwargs, status, templates", AUTH_WITHOUT_CONTACT)
@mark.django_db
def test_reach_pages_user_authenticated_without_contact(
        client_auth,
        sample_user_zoe,
        url,
        kwargs,
        templates,
        status,
):

    client = client_auth
    response = client.get(reverse(url, kwargs=kwargs))

    assert response.status_code == status
    assert [t.name for t in response.templates] == templates


# #############################################################################
#   log.models.__str__()
# #############################################################################
@mark.django_db
def test_entry__str__(client_auth, entry_list, sample_entries):
    entry = Entry.objects.get(desc=sample_entries[0]['desc'])

    assert entry.__str__() == sample_entries[0]['title']


# #############################################################################
#   log.models.all()
#############################################################################
@mark.django_db
def test_entry_all(client_auth, entry_list, sample_entries):
    entry = Entry.objects.get(title=sample_entries[0]['title'])
    entry_dict = entry.all()

    for label, field in sample_entries[0].items():
        assert entry_dict[label] == field
