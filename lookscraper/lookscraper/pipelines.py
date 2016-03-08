# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from looksdigest.models import Look, Location


class LookscraperPipeline(object):

    def process_look(self, item):
        if 'city' not in item:
            location_item, created = Location.objects.get_or_create(city=None, country=item['country'])
        else:
            location_item, created = Location.objects.get_or_create(city=item['city'], country=item['country'])

        if created is True:
            location_item.save()

        try:
            look_item = Look.objects.get(orig_id=item['orig_id'])
        except Look.DoesNotExist:
            look_item = Look(
                title=item['title'],
                img_url=item['img_url'],
                desc=item['desc'],
                orig_id=item['orig_id'],
                orig_hype=item['orig_hype'],
                location=location_item
            )
            look_item.save()

    def process_item(self, item, spider):
        self.process_look(item)
        # item.save()
        return item
