# -*- coding: utf-8 -*-
from {{ project_name }}.settings.base import *


# Debugging
# -----------------------------------------------------------------------------
DEBUG = TEMPLATE_DEBUG = True

# Databases
# -----------------------------------------------------------------------------
#DATABASES['default']['NAME'] = '{{ project_name }}_development'

# Email
# -----------------------------------------------------------------------------
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# Applications
# -----------------------------------------------------------------------------
INSTALLED_APPS += (
    'debug_toolbar',
)

# django-debug-toolbar
# -----------------------------------------------------------------------------
INTERNAL_IPS = ('127.0.0.1', )
MIDDLEWARE_CLASSES += ('debug_toolbar.middleware.DebugToolbarMiddleware',)
DEBUG_TOOLBAR_CONFIG = {'INTERCEPT_REDIRECTS': False}
