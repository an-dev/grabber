import sys
import os
import logging

from distutils.util import strtobool

from fabric.api import *
from fabric.contrib import django


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
    @task(alias=function.__name__)
    def wrap_function(*args, **kwargs):
        if len(args) > 0 and 'env' in kwargs:
            raise TypeError('%s() got multiple values for keyword argument "env"' % function.__name__)

        if len(args) > 0:
            environ = args[0]
        else:
            if 'env' in kwargs:
                environ = kwargs['env']
            else:
                environ = DEFAULT_ENV

        django.settings_module('{}.config.settings.{}'.format(DJANGO_PROJECT, environ))

        try:
            logger.debug('args = %s' % str(args))
            logger.debug('kwargs = %s' % str(kwargs))
            return function(*args, **kwargs)
        except Exception as e:
            raise e

    wrap_function.__doc__ = function.__doc__

    return wrap_function


@set_fab_env
def runserver(environ=DEFAULT_ENV, autoreload=True):
    """
        Runserver task, takes in env, autoreload(bool)
    """
    # TODO: get address:port from CLI
    if booleanize(autoreload):
        local('python manage.py runserver')

    if not booleanize(autoreload):
        local('python manage.py runserver --noreload')


@set_fab_env
def shell(environ=DEFAULT_ENV):
    """
        IPython Shell task
    """
    local('python manage.py shell -i ipython')


@set_fab_env
def migrate(environ=DEFAULT_ENV):
    """
        Migrate task
    """
    local('python manage.py migrate --run-syncdb')


@set_fab_env
def make_migrations(environ=DEFAULT_ENV):
    """
        Create Migration task
    """
    local('python manage.py makemigrations')
