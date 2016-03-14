from looksdigest.models import Look, Location

from datetime import datetime, timedelta


class LookscraperPipeline(object):

    @classmethod
    def parse_orig_date(cls, string_val):
        """Return a timedelta object from a string value (e.g.: 4 minutes).
        :type string_val: string
        """

        val, time_unit = string_val.split(' ')
        val = int(val)

        time_unit_deltas = {
            'seconds': timedelta(seconds=val),
            'minutes': timedelta(minutes=val),
            'hours': timedelta(hours=val)
        }

        # cast string to multiple (minute -> minutes)
        if time_unit in ['second', 'minute', 'hour']:
            time_unit += '%s' % 's'

        return time_unit_deltas.get(time_unit)

    def process_look(self, item):
        if 'city' not in item:
            location_item, created = Location.objects.get_or_create(city=None, country=item['country'])
        else:
            location_item, created = Location.objects.get_or_create(city=item['city'], country=item['country'])

        if created is True:
            location_item.save()

        try:
            _ = Look.objects.get(orig_id=item['orig_id'])
        except Look.DoesNotExist:
            look_item = Look(
                title=item['title'],
                img_url=item['img_url'],
                desc=item['desc'],
                orig_id=item['orig_id'],
                orig_hype=item['orig_hype'],
                location=location_item
            )

            if self.parse_orig_date(item['orig_date']) is not None:
                orig_date = datetime.now() - self.parse_orig_date(item['orig_date'])
                look_item.orig_date = orig_date

            look_item.save()

    def process_item(self, item, spider):
        self.process_look(item)
        return item
