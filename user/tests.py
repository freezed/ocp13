from pytest import fixture, mark

from django.contrib.auth.models import User
from django.test import Client
from django.urls import reverse


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


# #############################################################################
#   user.views.{UserDetail|UserUpdate}()
# #############################################################################
@mark.parametrize(
    "url", [('user:detail'), ('user:update')]
)
@mark.django_db
def test_reach_pages_anonymous(client_anon, url):
    response = client_anon.get(reverse(url))

    assert response.status_code == 302
    assert reverse('login') in response.url


@mark.parametrize(
    "url, templates", [
        ('user:detail', ['auth/user_detail.html', 'base.html']),
        ('user:update', ['auth/user_form.html', 'base.html']),
    ]
)
@mark.django_db
def test_index_authenticated_without_contacts(
        client_auth,
        sample_user_zoe,
        url,
        templates,
):

    client = client_auth
    response = client.get(reverse(url))
    user = sample_user_zoe

    assert response.status_code == 200
    assert [t.name for t in response.templates][:2] == templates
    assert response.context['user'].username == user['username']

    # TODO #27 : Add tests with contacts created
    if url == 'user:detail':
        assert response.context['date_joined']
        assert response.context['last_login']
        assert not response.context['last_contact']
