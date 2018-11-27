"""
`settings.py` for staging environement
Django settings for ocp13 project.
"""
from . import *

DEBUG = False
SECRET_KEY = os.environ.get('SECRET_KEY')

ALLOWED_HOSTS = ['ocp13-1664.herokuapp.com']
