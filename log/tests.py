from pytest import fixture

from django.test import Client
from django.urls import reverse


# #############################################################################
# ##     Fixtures
# #############################################################################
@fixture
def client_anon():
    """ Provide a Django test client """
    return Client()


# #############################################################################
#   log.views.{UserDetail|UserUpdate}()
# #############################################################################
def test_reach_pages_anonymous(client_anon):
    response = client_anon.get(
        reverse('lead:log:create', kwargs={'contact_id': 1})
    )

    assert response.status_code == 302
    assert reverse('login') in response.url
