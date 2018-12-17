from pytest import fixture, mark

from django.contrib.auth.models import User
from django.contrib import auth
from django.test import Client
from django.urls import reverse

### ############################################################################
###     Templates list used in various application templates
### ############################################################################
t_signup = [
    'registration/signup.html',
    'base.html',
    'a14n/anonymous.html',
    'a14n/form.html',
    'django/forms/widgets/text.html',
    'django/forms/widgets/input.html',
    'django/forms/widgets/attrs.html',
    'django/forms/widgets/password.html',
    'django/forms/widgets/input.html',
    'django/forms/widgets/attrs.html',
    'django/forms/widgets/password.html',
    'django/forms/widgets/input.html',
    'django/forms/widgets/attrs.html',
]

t_login = [
    'registration/login.html',
    'base.html',
    'a14n/anonymous.html',
    'a14n/form.html',
    'django/forms/widgets/text.html',
    'django/forms/widgets/input.html',
    'django/forms/widgets/attrs.html',
    'django/forms/widgets/password.html',
    'django/forms/widgets/input.html',
    'django/forms/widgets/attrs.html',
]

t_logout = [
    'registration/logged_out.html',
    'base.html',
    'a14n/anonymous.html',
]


### ############################################################################
###     Fixtures
### ############################################################################
@fixture
def client_anonymous():
    """ Provide a Django test client """
    return Client()


### ############################################################################
###     TESTING pages acces & templates : signup(),login(),logout()
### ############################################################################
@mark.parametrize("url, templates", [
    ('signup', t_signup),
    ('login',t_login),
    ('logout',t_logout),
])
def test_reach_conform_pages(client_anonymous, url, templates):
    """ Tests if all app page are reachable & use attendend templates"""
    response = client_anonymous.get(reverse(url))

    assert response.status_code == 200
    assert templates == [t.name for t in response.templates]


### ############################################################################
###     TESTING pages function : signup()
### ############################################################################
@mark.parametrize("pass1, pass2", [
    ("alice", "alice"),
    ("alicepass", "alicepass"),
    ("pass", "pass"),
    ("1234", "pass"),
    ("123456789", "123456789"),
])
@mark.django_db
def test_signup_unvalid_password(client_anonymous, pass1, pass2):
    """ Test wrong password combinaison """

    response = client_anonymous.post(
        reverse('signup'), {
            'username': 'alice',
            'password1': pass1,
            'password2': pass2,
        },
    )

    assert not User.objects.all().exists()


@mark.django_db
def test_signup_valid(client_anonymous):
    response = client_anonymous.post(
        reverse('signup'), {
            'username': 'alice',
            'password1': '@lice1234',
            'password2': '@lice1234',
        },
        follow=True,
    )
    assert response.wsgi_request.user.is_authenticated
    assert 'alice' == User.objects.get(id=1).username
    assert (reverse('user:index'), 302) == response.redirect_chain[0]
    assert ['user/index.html', 'base.html'] == [t.name for t in response.templates]


### ############################################################################
###     TESTING pages function : login()
### ############################################################################
@mark.django_db
def test_login_valid(client_anonymous):
    USER = {'username': 'bob','password': 'bobbobbob'}
    User.objects.create_user(**USER)

    response = client_anonymous.post(reverse('login'), USER, follow=True)
    user = auth.get_user(response.wsgi_request)

    assert user.is_authenticated
    assert user.username == USER['username']
    assert ['404.html', 'base.html'] == [t.name for t in response.templates]


@mark.parametrize("url, templates", [
    ('login',t_login),
])
@mark.django_db
def test_login_unvalid(client_anonymous, url, templates):
    USER = {'username': 'bob','password': 'bobbobbob'}
    User.objects.create_user(**USER)

    response = client_anonymous.post(
        reverse(url),
        {'username': 'foo','password': 'bar'},
        follow=True,
    )
    user = auth.get_user(response.wsgi_request)

    assert user.is_anonymous
    assert [t.name for t in response.templates] == templates
