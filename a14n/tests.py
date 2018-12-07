from pytest import fixture, mark

from django.test import Client
from django.contrib.auth.models import User

@fixture
def CLIENT():
    """ Provide a Django test client """
    return Client()


################################################################################
#   a14n.signup()
################################################################################
def test_reach_signup_page(CLIENT):
    """ Sign-up page is reachable """

    templates = [
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
        'django/forms/widgets/attrs.html'
    ]
    response = CLIENT.get('/my/signup/')

    assert response.status_code == 200
    assert templates == [t.name for t in response.templates]


@mark.parametrize("pass1, pass2", [
    ("alice", "alice"),
    ("alicepass", "alicepass"),
    ("pass", "pass"),
    ("1234", "pass"),
    ("123456789", "123456789"),
])
@mark.django_db
def test_signup_unvalid_password(CLIENT, pass1, pass2):
    """ Test wrong password combinaison """

    response = CLIENT.post(
        '/my/signup/', {
            'username': 'alice',
            'password1': pass1,
            'password2': pass2,
        },
    )

    assert not User.objects.all().exists()


@mark.django_db
def test_signup_valid(CLIENT):
    response = CLIENT.post(
        '/my/signup/', {
            'username': 'alice',
            'password1': '@lice1234',
            'password2': '@lice1234',
        },
        follow=True,
    )

    assert 'alice' == User.objects.get(id=1).username
    assert ('/', 302) == response.redirect_chain[0]
    assert ['home.html', 'base.html'] == [t.name for t in response.templates]


################################################################################
#   a14n.logout()
################################################################################

################################################################################
#   a14n.login()
################################################################################
