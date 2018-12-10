from pytest import fixture, mark

from django.contrib.auth.models import User
from django.test import Client
from django.urls import reverse


### ############################################################################
###     Fixtures
### ############################################################################
@fixture
def CLIENT():
    """ Provide a Django test client """
    return Client()

@fixture
def USER():
    USER = {'username': 'bob','password': 'bobbobbob'}
    return USER


################################################################################
#   lead.views.index()
################################################################################
def test_reach_index_anonymous(CLIENT):
    response = CLIENT.get(reverse('lead-index'))

    assert response.status_code == 302
    assert response.url == reverse('login')
    assert response.templates == []


@mark.django_db
def test_reach_index_authenticated(CLIENT, USER):
    user = User.objects.create_user(**USER)
    response = CLIENT.force_login(user)
    response = CLIENT.get(reverse('lead-index'))

    assert response.status_code == 200
    assert [t.name for t in response.templates] == [
        'lead/index.html',
        'base.html'
    ]
