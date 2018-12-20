from os import environ
from os.path import dirname, join

import dj_database_url

import sentry_sdk

from sentry_sdk.integrations.django import DjangoIntegration

from .base import *
from rejuvahome.libs.aws.conf import *

DEBUG = False
TEMPLATES[0]['OPTIONS']['debug'] = False

EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'kirancapoor94@gmail.com'
EMAIL_HOST_PASSWORD = environ.get('EMAIL_HOST_PASSWORD')
EMAIL_PORT = 587
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = 'Rejuva Website <kiran.capoor94@gmail.com>'
BASE_URL = 'https://www.rejuvaaesthetica.com/'


MANAGERS = (
    ('Kiran Capoor', "kiran.capoor94@gmail.com"),
)

ADMINS = MANAGERS


SECRET_KEY = environ.get('DJANGO_SECRET_KEY')


ALLOWED_HOSTS = ['rejuvahome.herokuapp.com',
                 'www.rejuvaaesthetica.com', '.rejuvaaesthetica.com']

INSTALLED_APPS += (
    # 'django.contrib.sitemaps',
    'storages',
    'django_summernote',
    'apps.pages',
    'apps.blogs',
    'apps.tags',
    'apps.users',
    'apps.gallery',

)

# Database
DATABASES = {
    'default': dj_database_url.config(default='')
}

# Logging
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "handlers": {
        "console": {
            "level": "INFO",
            "class": "logging.StreamHandler",
        },
    },
    "loggers": {
        "django": {
            "handlers": ["console"],  # "null"
            "propagate": True,
            "level": "WARNING",
        },
        "django.request": {
            "handlers": ["console"],
            "level": "WARNING",  # "ERROR"
            "propagate": False,
        },
        "django.db.backends": {
            "handlers": ["console"],
            "propagate": False,
            "level": "WARNING",
        },

        "apps": {
            "handlers": ["console"],
            "level": "WARNING",
            "propagate": False,
        },
    }
}


sentry_sdk.init(
    dsn="https://54e7a5f240404bde88c265d8f13696e8@sentry.io/1317729",
    integrations=[DjangoIntegration()]
)

# Let's Encrypt ssl/tls https

CORS_REPLACE_HTTPS_REFERER      = True
HOST_SCHEME                     = "https://"
SECURE_PROXY_SSL_HEADER         = ('HTTP_X_FORWARDED_PROTO', 'https')
SECURE_SSL_REDIRECT             = True
SESSION_COOKIE_SECURE           = True
CSRF_COOKIE_SECURE              = True
SECURE_HSTS_INCLUDE_SUBDOMAINS  = True
SECURE_HSTS_SECONDS             = 1000000
SECURE_FRAME_DENY               = True
