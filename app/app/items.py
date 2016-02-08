# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class LookItem(scrapy.Item):
	look_id 	= scrapy.Field()
	title 		= scrapy.Field()
	img_url		= scrapy.Field() 
	desc 		= scrapy.Field() 
	orig_hype 	= scrapy.Field()


class LocationItem(scrapy.Item):
	city    = scrapy.Field()
	country = scrapy.Field()
