"""
`settings.py` for staging environement
Django settings for ocp13 project.
"""
import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration

from . import *

DEBUG = False
SECRET_KEY = os.environ.get('SECRET_KEY')

ALLOWED_HOSTS = ['ocp13-1664.herokuapp.com']

sentry_sdk.init(
    dsn="https://9f531f2ee4354cd09dcbd64066283928@sentry.io/1331802",
    integrations=[DjangoIntegration()],
    environment="staging",
)
