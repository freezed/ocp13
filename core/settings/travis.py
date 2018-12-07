"""
`settings.py` for travis CI
Django settings for ocp13 project.
"""
from . import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'HOST': '',
        'PORT': '',
        'NAME': '',
        'USER': 'postgres',
        'PASSWORD':'',
    }
}
