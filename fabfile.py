import sys
import os
from fabric.api import *
from fabric.contrib import django
from distutils.util import strtobool

if not os.path.isfile('./fabfile.py'):
    print '*****Error, you must be in the root directory for running fab commands*****'
    sys.exit(1)

# ------------------------------
# Fabric management functions
# ------------------------------

DJANGO_PROJECT = 'looksdigest'
DEFAULT_ENV = 'dev'
django.project(DJANGO_PROJECT)


def booleanize(val):
    if type(val) is bool:
        return val
    return strtobool(val) is 1


def set_fab_env(function):
    def wrap_function(*args, **kwargs):
        env = DEFAULT_ENV

        if len(args) > 0 and 'env' in kwargs:
            raise TypeError('%s() got multiple values for keyword argument "env"' % function.__name__)

        if len(args) > 0:
            env = args[0]
        else:
            if 'env' in kwargs:
                env = kwargs['env']

        django.settings_module('{}.config.settings.{}'.format(DJANGO_PROJECT, env))

        try:
            print args, kwargs
            return function(*args, **kwargs)
        except Exception as e:
            raise e
    return wrap_function


@set_fab_env
def runserver(env=DEFAULT_ENV, autoreload=True):

    # switch environment and get address:port from there
    if booleanize(autoreload):
        local('python manage.py runserver')

    if not booleanize(autoreload):
        local('python manage.py runserver --noreload')


@set_fab_env
def migrate():
    local('python manage.py migrate')
