# -*- coding: utf-8 -*-

# Scrapy settings for lookscraper project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html


import os
from random import randrange

import django
from django.conf import settings


BOT_NAME = 'lookscraper'

SPIDER_MODULES = ['lookscraper.spiders']
NEWSPIDER_MODULE = 'lookscraper.spiders'

USER_AGENTS = [
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_3) AppleWebKit/601.4.4 (KHTML, like Gecko) Version/9.0.3 Safari/601.4.4',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.109 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:44.0) Gecko/20100101 Firefox/44.0'
]

USER_AGENT = USER_AGENTS[randrange(3)]

CONCURRENT_REQUESTS = 2
DOWNLOAD_DELAY      = 1

# Configure item pipelines
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html

ITEM_PIPELINES = {
    'lookscraper.pipelines.LookscraperPipeline': 300,
}


# ENV = os.environ.get("SCRAPY_ENV")
DJANGO_PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import sys
sys.path.append(DJANGO_PROJECT_DIR)
os.environ['DJANGO_SETTINGS_MODULE'] = '{}.config.settings.{}'.format('looksdigest', 'dev')
# logger = logging.getLogger(__name__)
# if ENV == 'prod':
#     logger.setLevel(level=logging.INFO)
#
# if ENV == 'dev':
#     logger.setLevel(level=logging.DEBUG)

django.setup()
