from pytest import fixture

from django.contrib.staticfiles import finders
from django.test import Client

@fixture
def templates():
    """ set basic template """
    templates = ['base.html']

    return templates

################################################################################
#   core.views.home()
################################################################################
def test_home(templates):
    templates.insert(0, 'home.html')
    CLIENT = Client()
    response = CLIENT.get('/')

    assert response.status_code == 200
    assert templates == [t.name for t in response.templates]


################################################################################
#   core.views.about()
################################################################################
def test_about():
    CLIENT = Client()
    response = CLIENT.get('/about')

    assert response.status_code == 200
    assert "Hopla, Seppi bring a Wurschtsalat avec un amer!" == response.content.decode()


################################################################################
#   static.css.*
################################################################################
def test_style_css():
    assert finders.find('favico.ico') != None
    assert finders.find('img/favico.png') != None
    assert finders.find('css/styles.css') != None
    assert finders.find('css/knacss.css') != None
    assert finders.find('css/foobar.css') == None


################################################################################
#   core.views - error
################################################################################

def test_404():
    CLIENT = Client()
    response = CLIENT.get('/foo')

    assert response.status_code == 404
################################################################################
