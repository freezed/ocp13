from pytest import fixture, mark

from django.contrib.auth.models import User
from django.test import Client
from django.urls import reverse

from lead.models import Contact


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
        *sample_contacts[0].keys()
    ).all().order_by('-id')


# #############################################################################
#   lead.views.index()
# #############################################################################
def test_reach_index_anonymous(client_anon):
    response = client_anon.get(reverse('lead-index'))

    assert response.status_code == 302
    assert response.url == reverse('login')
    assert response.templates == []


@mark.django_db
def test_reach_index_authenticated_without_contact(client_auth):
    response = client_auth.get(reverse('lead-index'))

    assert response.status_code == 200
    assert [t.name for t in response.templates] == [
        'lead/index.html',
        'base.html',
        'lead/none.html',
    ]


@mark.django_db
def test_reach_index_authenticated_with_contacts(
        client_auth,
        contact_list,
        sample_contacts
):
    response = client_auth.get(reverse('lead-index'))

    assert response.status_code == 200
    assert [t.name for t in response.templates] == [
        'lead/index.html',
        'base.html',
        'lead/list.html',
    ]

    for idx, contact in enumerate(sample_contacts):
        key_list = sample_contacts[idx]

        for k in key_list:
            assert contact_list[idx][k] == response.context['contacts'][idx][k]


# #############################################################################
#   lead.models.__str__()
# #############################################################################
@mark.django_db
def test_contact__str__(client_auth, contact_list, sample_contacts):
    contact = Contact.objects.get(email=sample_contacts[0]['email'])

    assert contact.__str__() == 'jean'


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
