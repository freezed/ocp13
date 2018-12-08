from pytest import fixture, mark

from django.contrib.auth.models import User
from django.test import Client
from django.urls import reverse

### ############################################################################
###     Templates list used in various application templates
### ############################################################################
t_signup = [
    'registration/signup.html',
    'base.html',
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
    'django/forms/widgets/text.html',
    'django/forms/widgets/input.html',
    'django/forms/widgets/attrs.html',
    'django/forms/widgets/password.html',
    'django/forms/widgets/input.html',
    'django/forms/widgets/attrs.html',
]

t_logout = [
    'registration/logged_out.html',
    'base.html'
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
    assert ('/', 302) == response.redirect_chain[0]
    assert ['home.html', 'base.html'] == [t.name for t in response.templates]
