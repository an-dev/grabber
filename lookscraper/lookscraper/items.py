from scrapy_djangoitem import DjangoItem

from looksdigest.models import Look, Location


class LookItem(DjangoItem):
    django_model = Look


class LocationItem(DjangoItem):
    django_model = Location
