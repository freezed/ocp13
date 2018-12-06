"""
`settings.py` for `heroku local web` command environement
Django settings for ocp13 project.
"""
import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration

from . import *

DEBUG = False
SECRET_KEY = 'HEROKU_LOCAL_3#-w$0tr9(e&o-'

ALLOWED_HOSTS = [
    '0.0.0.0',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

sentry_sdk.init(
    dsn="https://9f531f2ee4354cd09dcbd64066283928@sentry.io/1331802",
    integrations=[DjangoIntegration()],
    environment="heroku-local",
)

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
