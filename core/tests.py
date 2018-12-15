from pytest import fixture, mark

from django.contrib.staticfiles import finders
from django.test import Client

@fixture
def CLIENT():
    """ Provide a Django test client """
    return Client()


################################################################################
#   core.views
################################################################################
@mark.parametrize(
    "tmplt, url, status", [
        (['home.html', 'base.html', 'a14n/anonymous.html'], '/', 200),
        (['about.html', 'base.html', 'a14n/anonymous.html'], '/about', 301),
    ]
)
def test_home(CLIENT, tmplt, url, status):
    response = CLIENT.get(url)

    assert response.status_code == status
    # assert tmplt == [t.name for t in response.templates]
    print(response.templates)


################################################################################
#   core.views.hopla()
################################################################################
def test_hopla(CLIENT):
    response = CLIENT.get('/hopla')

    assert response.status_code == 200
    assert "Hopla, Seppi bring a Wurschtsalat avec un amer!" == response.content.decode()


################################################################################
#   static.css.*
################################################################################
@mark.parametrize("url", [
    ('favico.ico'),
    ('img/favico.png'),
    ('css/styles.css'),
    ('css/knacss.css'),
])
def test_valid_static_files(url):
    assert finders.find(url) != None

def test_unvalid_static_files():
    assert finders.find('css/foobar.css') == None
################################################################################
#   core.views - error
################################################################################

def test_404(CLIENT):
    response = CLIENT.get('/foo')

    assert response.status_code == 404
################################################################################
