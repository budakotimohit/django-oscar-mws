# Django settings for sandbox project.
import os


PROJECT_DIR = os.path.dirname(__file__)
location = lambda x: os.path.join(
    os.path.dirname(os.path.realpath(__file__)), "../%s" % x)

DEBUG = True
TEMPLATE_DEBUG = DEBUG

USE_LESS = True

ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(os.path.dirname(__file__), 'db.sqlite3'),
        'ATOMIC_REQUESTS': True,
    }
}

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = 'Australia/Melbourne'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-gb'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = location('public/media')

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = '/media/'

STATIC_URL = '/static/'

STATICFILES_DIRS = [
    location('static/'),
]

STATIC_ROOT = location('public')

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'compressor.finders.CompressorFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'sba9ti)x&amp;^fkod-g91@^_yi6y_#&amp;3mo#m5@n)i&amp;k+0h=+zsfkb'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.request",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.static",
    "django.contrib.messages.context_processors.messages",
    # Oscar specific
    'oscar.apps.search.context_processors.search_form',
    'oscar.apps.promotions.context_processors.promotions',
    'oscar.apps.checkout.context_processors.checkout',
    'oscar.apps.customer.notifications.context_processors.notifications',
    'oscar.core.context_processors.metadata',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.transaction.TransactionMiddleware',
    'oscar.apps.basket.middleware.BasketMiddleware',
)

ROOT_URLCONF = 'sandbox.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'sandbox.wsgi.application'

# Compressor and pre-compiler settings for django-compressor
USE_LESS = False

COMPRESS_ENABLED = False
COMPRESS_OFFLINE = False
COMPRESS_PRECOMPILERS = [('text/less', 'lessc {infile} {outfile}')]

COMPRESS_OFFLINE_CONTEXT = {
    'STATIC_URL': 'STATIC_URL',
    'use_less': USE_LESS,
}

from oscar import OSCAR_MAIN_TEMPLATE_DIR

TEMPLATE_DIRS = [
    location('templates'),
    os.path.join(OSCAR_MAIN_TEMPLATE_DIR, 'templates'),
    OSCAR_MAIN_TEMPLATE_DIR,
]

DJANGO_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.flatpages',
    'django.contrib.admin',

    'compressor',
    'south',
    'django_extensions',
]

from oscar import get_core_apps
INSTALLED_APPS = DJANGO_APPS + ['oscar_mws'] + get_core_apps([
    'partner',
])

AUTHENTICATION_BACKENDS = (
    'oscar.apps.customer.auth_backends.Emailbackend',
    'django.contrib.auth.backends.ModelBackend',
)

LOGIN_REDIRECT_URL = '/accounts/'
APPEND_SLASH = True

DEBUG_TOOLBAR_CONFIG = {
    'INTERCEPT_REDIRECTS': False
}

# Oscar settings
from oscar.defaults import *
from oscar_mws.defaults import *

OSCAR_ALLOW_ANON_CHECKOUT = True

OSCAR_SHOP_NAME = 'FancyPages Sandbox'
OSCAR_SHOP_TAGLINE = 'Make your pages sparkle and shine!'

# Haystack settings
HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.simple_backend.SimpleEngine',
    },
}

OSCAR_DASHBOARD_NAVIGATION += MWS_DASHBOARD_NAVIGATION

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
        }
    },
    'loggers': {
        'oscar_mws.api': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': True,
        },
        'django.request': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': True,
        },
    }
}

########## RUNSCOPE SETTINGS
RUNSCOPE_BUCKET_KEY = os.getenv('RUNSCOPE_BUCKET_KEY')
########## END RUNSCOPE SETTINGS
