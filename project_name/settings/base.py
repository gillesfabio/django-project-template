# -*- coding: utf-8
import os


# Project paths
# -----------------------------------------------------------------------------
PROJECT_PACKAGE = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
PROJECT_ROOT = os.path.abspath(os.path.join(PROJECT_PACKAGE, os.pardir))
PROJECT_NAME = os.path.basename(PROJECT_PACKAGE)

# Debugging
# -----------------------------------------------------------------------------
DEBUG = TEMPLATE_DEBUG = False

# Administrators
# -----------------------------------------------------------------------------
ADMINS = () # FIXME: set ADMINS in settings.py
MANAGERS = ADMINS

# Databases
# -----------------------------------------------------------------------------
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(PROJECT_ROOT, 'database.db'),
    }
}

# Site
# -----------------------------------------------------------------------------
SITE_ID = 1

# Timezone
# -----------------------------------------------------------------------------
TIME_ZONE = 'Europe/Paris' # FIXME: set TIME_ZONE in settings.py
USE_TZ = True

# I18n / L10n
# -----------------------------------------------------------------------------
LANGUAGE_CODE = 'en-us'
USE_I18N = True
USE_L10N = True
LOCALE_PATHS = (
    os.path.join(PROJECT_PACKAGE, 'locale'),
)

# Media
# -----------------------------------------------------------------------------
MEDIA_ROOT = os.path.join(PROJECT_ROOT, 'public', 'media')
MEDIA_URL = '/media/'

# Static
# -----------------------------------------------------------------------------
STATIC_ROOT = os.path.join(PROJECT_ROOT, 'public', 'static')
STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(PROJECT_PACKAGE, 'static'),
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

# Secret key
# -----------------------------------------------------------------------------
SECRET_KEY = '{{ secret_key }}' # FIXME: move SECRET_KEY in local.py

# Templates
# -----------------------------------------------------------------------------
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

TEMPLATE_DIRS = (
    os.path.join(PROJECT_PACKAGE, 'templates'),
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.contrib.messages.context_processors.messages',
    'django.core.context_processors.debug',
    'django.core.context_processors.media',
    'django.core.context_processors.request',
    'django.core.context_processors.i18n',
    'django.core.context_processors.static',
)

# Middleware
# -----------------------------------------------------------------------------
MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

# URLs
# -----------------------------------------------------------------------------
ROOT_URLCONF = u'%s.urls' % PROJECT_NAME

# WSGI
# -----------------------------------------------------------------------------
WSGI_APPLICATION = u'%s.wsgi.application' % PROJECT_NAME

# Fixtures
# -----------------------------------------------------------------------------
FIXTURE_DIRS = (
    os.path.join(PROJECT_PACKAGE, 'fixtures'),
)

# Cache
# -----------------------------------------------------------------------------
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
    }
}

# Applications
# -----------------------------------------------------------------------------
INSTALLED_APPS = (
    # Django
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'django.contrib.webdesign',

    # External apps
    'pipeline',
    'south',

    # Project apps
    #'{{ project_name }}.myapp',
)

# Logging
# -----------------------------------------------------------------------------
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'simple': {
            'format': '%(asctime)s %(levelname)s: %(message)s',
        },
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        },
    },
    'loggers': {
        'django.request': {
            'handlers': ['console'],
            'level': 'ERROR',
            'propagate': True,
        },
        '{{ project_name }}': {
            'handlers': ['console'],
            'level': 'INFO',
        },
    },
}

# django-pipeline
# -----------------------------------------------------------------------------
MIDDLEWARE_CLASSES += ('pipeline.middleware.MinifyHTMLMiddleware',)
STATICFILES_STORAGE = 'pipeline.storage.PipelineCachedStorage'
PIPELINE_CSS = {
    'master': {
        'source_filenames': (
            'site/css/main.css',
        ),
        'output_filename': '{{ project_name }}/css/master.css',
    },
}
PIPELINE_JS = {
    'master': {
        'source_filenames': (
            'site/js/main.js',
        ),
        'output_filename': '{{ project_name }}/js/master.js',
    },
}

# django-maintenancemode
# ----------------------------------------------------------------------
MIDDLEWARE_CLASSES += ('maintenancemode.middleware.MaintenanceModeMiddleware',)
MAINTENANCE_MODE = False
