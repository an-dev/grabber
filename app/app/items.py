# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class AppItem(scrapy.Item):
	look_id = scrapy.Field();
	url  		= scrapy.Field() 
	desc 		= scrapy.Field() 
	orig_hype 	= scrapy.Field()
	#site_hype
	user_id(fk) = scrapy.Field() 
