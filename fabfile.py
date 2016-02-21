import sys
import os
from fabric.api import *
from fabric.contrib import django
from distutils.util import strtobool
import logging

logger = logging.getLogger(__name__)

if not os.path.isfile('./fabfile.py'):
    print '*****Error, you must be in the root directory for running fab commands*****'
    sys.exit(1)

DJANGO_PROJECT = 'looksdigest'
DEFAULT_ENV = 'dev'
django.project(DJANGO_PROJECT)


def booleanize(val):
    if type(val) is bool:
        return val
    return strtobool(val) is 1


def set_fab_env(function):
    """
        Custom decorator to import specific env
    """
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
            logger.debug('args = %s' % str(args))
            logger.debug('kwargs = %s' % str(kwargs))
            return function(*args, **kwargs)
        except Exception as e:
            raise e
    return wrap_function


@set_fab_env
def runserver(env=DEFAULT_ENV, autoreload=True):
    """
        Runserver task
        @env: environment in which to run the server
        @autoreload: wheather to use or not --noreload flag
    """
    # TODO: get address:port from CLI
    if booleanize(autoreload):
        local('python manage.py runserver')

    if not booleanize(autoreload):
        local('python manage.py runserver --noreload')


@set_fab_env
def migrate():
    """
        Migrate task
    """
    # TODO: migrate per app
    local('python manage.py migrate')
