import logging

from scrapy import Spider

from ..settings import logger
from ..items import LookItem, LocationItem

# setting __name__ parameter
logger  = logging.getLogger(__name__)


class LookSpider(Spider):
    name = 'lookspider'
    start_urls = [
        'http://lookbook.nu/preference/look-hot-sort/popular'
    ]

    def parse_look(self, look):
        item = LookItem()
        # item['look_id']   = look.xpath('@id').extract()[0]
        # item['title']     = look.xpath('div[@class="look_meta_container"]/h1/a/text()').extract()[0]

        # get directly num id and strip rest of string
        id = look.xpath('@id').extract()[0].strip('look_')

        item['look_id'] = id
        item['title'] = look.xpath('//a[@id="look_title_' + id + '"]/text()').extract()[0]
        item['img_url'] = look.xpath('//a[@id="photo_' + id + '"]/img/@src').extract()[0]
        item['desc'] = look.xpath('//a[@id="photo_' + id + '"]/img/@alt').extract()[0].split(' - ')[1]
        item['orig_hype'] = \
            look.xpath('div[@class="look_hype_container"]/div[@data-look-id="' + id + '"]/@data-hypes-count').extract()[0]
        return item

    def parse_location(self, look):
        item = LocationItem()
        try:
            item['city'] = look.xpath(
                'div[@class="look_meta_container"]/p/a[starts-with(@data-page-track,"location")]/text()').extract()[0]
        except IndexError:
            logger.warn("No city for this one.")
        item['country'] = \
            look.xpath(
                'div[@class="look_meta_container"]/p/a[starts-with(@data-page-track,"country")]/text()').extract()[0]
        return item

    def parse(self, response):
        for look in response.xpath('//li[starts-with(@id,"look_")]'):
            yield self.parse_look(look)
            yield self.parse_location(look)
