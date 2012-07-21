# -*- coding: utf-8 -*-

VERSION = (0, 1)

def get_version():
    """
    Returns version as a string.
    """
    return '.'.join(map(str, VERSION))

__version__ = get_version()

try:
    from django.template.loader import add_to_builtins
    add_to_builtins('django.templatetags.i18n')
    add_to_builtins('django.templatetags.future')
    add_to_builtins('django.templatetags.tz')
except ImportError:
    pass
