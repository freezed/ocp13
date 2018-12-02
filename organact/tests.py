import pytest

from django.test import Client

################################################################################
#   organact.views.home()
################################################################################
def test_home():
    CLIENT = Client()
    response = CLIENT.get('/')

    assert response.status_code == 200

def test_404():
    CLIENT = Client()
    response = CLIENT.get('/foo')

    assert response.status_code == 404
################################################################################
