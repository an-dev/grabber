import logging
# importing logger from settings
from app.settings import logger

# setting __name__ parameter
logger = logging.getLogger(__name__)

from scrapy import Spider


class AppSpider(Spider):
	name = 'app'
	start_urls = ['http://lookbook.nu/']

	def parse(self, response):
		logger.debug(response.url)

