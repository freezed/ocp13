"""
`settings.py` for staging environement
Django settings for ocp13 project.
"""
import dj_database_url

import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration

from . import *

DEBUG = False
SECRET_KEY = os.environ.get('SECRET_KEY')

ALLOWED_HOSTS = [
    'ocp13-1664.herokuapp.com',
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
    environment="staging",
)

DATABASES = {
    'default': dj_database_url.config(conn_max_age=600, ssl_require=True)
}

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
