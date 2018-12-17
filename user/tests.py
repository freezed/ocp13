from pytest import fixture, mark

from django.contrib.auth.models import User
from django.test import Client


@fixture
def dt_client():
    """ Provide a Django test client """
    return Client()


# #############################################################################
#   user.views.index()
# #############################################################################
@mark.parametrize(
    "templates, url", [
        (['auth/user_detail.html', 'base.html'], '/user/'),
    ]
)
@mark.django_db
def test_index_authenticated(dt_client, templates, url):
    USER = {
        'username': 'alice',
        'password': '@lice1234',
    }

    test_user = User.objects.create_user(**USER)
    dt_client.force_login(test_user)
    response = dt_client.get(url)

    assert response.status_code == 200
    assert [t.name for t in response.templates] == templates
    assert response.context['user'].username == USER['username']
    assert response.context['date_joined']
    assert response.context['last_login']


def test_index_anonymous(dt_client):
    response = dt_client.get('/user/')

    assert response.wsgi_request.user.is_anonymous
    assert response.status_code == 302
    assert response.url == '/my/login/?next=/user/'
