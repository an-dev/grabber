from looksdigest.config.settings.base import *

DJANGO_SETTINGS_MODULE = 'looksdigest.config.settings.dev'
ENV = 'dev'
loader = LoadConf(ENV)
# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': loader.get_secret('DJANGO_DB_ENGINE'),
        'NAME': loader.get_secret('DJANGO_DB_NAME'),
        'USER': loader.get_secret('DJANGO_DB_USER'),
        'PASSWORD': loader.get_secret('DJANGO_DB_PASSWORD'),
        'HOST': loader.get_secret('DJANGO_DB_HOST'),
        'PORT': loader.get_secret('DJANGO_DB_PORT')
    }
}
