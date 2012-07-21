## Prerequisites

Install [pip](http://www.pip-installer.org/) and [virtualenvwrapper](http://www.doughellmann.com/docs/virtualenvwrapper/):

    sudo easy_install pip
    pip install virtualenvwrapper
    echo "source /usr/local/bin/virtualenvwrapper.sh" >> ~/.bash_profile
    source ~/.bash_profile

Create a dedicated virtualenv for [Django](http://djangoproject.com):

    mkvirtualenv django
    pip install django

You've done.

## Installation

Be sure your current virtualenv is `django`:

    workon django

Create your Django project with the `--template` argument pointing on the GitHub
zipball of the branch you want to grab (and with `--extension` argument to parse
Python and reStructuredText files):

    django-admin.py startproject PROJECT_NAME --template=https://github.com/gillesfabio/django-project-template/zipball/BRANCH --extension=py,rst

Deactivate the Django virtualenv:

    deactivate

Create a virtualenv for your Django project:

    mkvirtualenv PROJECT_NAME

Install requirements:

    pip install -r PROJECT_NAME/requirements/development.txt

Rename `PROJECT_NAME/settings/local.sample.py`:

    mv PROJECT_NAME/PROJECT_NAME/settings
    mv local.sample.py local.py

Import settings for the given environment:

    from PROJECT_NAME.settings.development import *

Override settings if you need.

Sychronize and run the server:

    python manage.py syncdb
    python manage.py runserver

Celebrate!

## Requirements and version numbers

This Django project template does not use explicit version numbers for requirements to get the latest stable version at project creation.

Edit requirement files (in `requirements` directory) and add version numbers to your requirements. Never ever use requirements without explicit version numbers. This can kill your project.

Use `pip freeze` to catch version numbers in a second:

    pip freeze > freeze.txt

So don't forget to update your requirements.

## Branches

### master

Only contains this README file.

### simple

Stack:

* [Django](http://djangoproject.com/)
* [PIL](http://www.pythonware.com/products/pil/)
* [SQLite](http://www.sqlite.org/)
* [South](http://south.aeracode.org/)
* [Sphinx](http://sphinx.pocoo.org/)
* [django-pipeline](https://github.com/cyberdelia/django-pipeline/)
* [django-maintenancemode](https://github.com/shanx/django-maintenancemode/)
* [django-debug-toolbar](https://github.com/django-debug-toolbar/django-debug-toolbar/)

### bootstrap

The `simple` stack +:

* [Twitter Bootstrap](http://twitter.github.com/bootstrap/)
* [jQuery](http://jquery.com)
* [django-bootstrap-toolkit](https://github.com/dyve/django-bootstrap-toolkit/)
