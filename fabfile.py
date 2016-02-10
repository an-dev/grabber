import sys
import os
from fabric.api import *
from fabric.contrib import django

if not os.path.isfile('./fabfile.py'):
    print '*****Error, you must be in the root directory for running fab commands*****'
    sys.exit(1)

# ------------------------------
# Fabric management functions
# ------------------------------

DJANGO_PROJECT = 'looksdigest'
django.project(DJANGO_PROJECT)


def set_fab_env(env):
    django.settings_module('{}.config.settings.{}'.format(DJANGO_PROJECT, env))


def runserver(env='dev', autoreload=True):
    # switch environment and get address:port from there
    set_fab_env(env)
    if autoreload is True:
        local('python manage.py runserver')

    if autoreload is False:
        local('python manage.py runserver --noreload')
