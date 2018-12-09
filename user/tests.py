from pytest import fixture, mark

from django.contrib.auth.models import User
from django.test import Client

@fixture
def CLIENT():
    """ Provide a Django test client """
    return Client()


################################################################################
#   user.views.index()
################################################################################
@mark.parametrize(
    "templates, url", [
        (['user/index.html', 'base.html'], '/user/'),
    ]
)
@mark.django_db
def test_index_authenticated(CLIENT, templates, url):
    USER = {
        'username': 'alice',
        'password': '@lice1234',
    }

    test_user = User.objects.create_user(**USER)
    CLIENT.force_login(test_user)
    response = CLIENT.get(url)

    assert response.status_code == 200
    assert [t.name for t in response.templates] == templates
    assert response.context['user'].username == USER['username']
    assert response.context['date_joined']
    assert response.context['last_login']


def test_index_anonymous(CLIENT):
    response = CLIENT.get('/user/')

    assert response.wsgi_request.user.is_anonymous
    assert response.status_code == 302
    assert response.url == '/'
