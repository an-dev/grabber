# import logging

from scrapy import Spider, Request

# from ..settings import logger
from ..items import LookItem

# setting __name__ parameter
# logger  = logging.getLogger(__name__)


class LookSpider(Spider):
    name = 'lookspider'
    start_urls = [
        'http://lookbook.nu/new'
    ]
    cookies = [{
        'name': 'look-list-karma',
        'value': 'first_looks'
    }]

    def start_requests(self):
        for url in self.start_urls:
            yield Request(cookies=self.cookies, url=url)

    def parse_look(self, look):
        # first example
        # item['look_id']   = look.xpath('@id').extract()[0]
        # item['title']     = look.xpath('div[@class="look_meta_container"]/h1/a/text()').extract()[0]

        item = LookItem()

        # get directly num id and strip rest of string
        orig_id = look.xpath('@id').extract()[0].strip('look_')

        item['orig_id'] = orig_id
        item['title'] = look.xpath('//a[@id="look_title_' + orig_id + '"]/text()').extract()[0]
        item['img_url'] = look.xpath('//a[@id="photo_' + orig_id + '"]/img/@src').extract()[0]
        item['desc'] = look.xpath('//a[@id="photo_' + orig_id + '"]/img/@alt').extract()[0].split(' - ')[1]
        item['orig_hype'] = look.xpath(
            'div[@class="look_hype_container"]/div[@data-look-id="' + orig_id + '"]/@data-hypes-count').extract()[0]

        try:
            item['city'] = look.xpath(
                'div[@class="look_meta_container"]/p/a[starts-with(@data-page-track,"location")]/text()').extract()[0]
        except IndexError:
            print 'No city for this one.'
            # logger.warn("No city for this one.")
        item['country'] = \
            look.xpath(
                'div[@class="look_meta_container"]/p/a[starts-with(@data-page-track,"country")]/text()').extract()[0]
        return item

    def parse(self, response):
        for look in response.xpath('//li[starts-with(@id,"look_")]'):
            yield self.parse_look(look)
