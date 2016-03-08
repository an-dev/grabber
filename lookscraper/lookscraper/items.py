from scrapy import Field
from scrapy_djangoitem import DjangoItem
from looksdigest.models import Look


class LookItem(DjangoItem):
    django_model = Look
    city         = Field()
    country      = Field()
