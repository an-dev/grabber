from django.db import models


class TimestampedModel(models.Model):
    """
        An abstract base class model that provides
        self-updating ``created`` and ``modified`` fields.
    """
    created  = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        # abstract True to prevent creating unnecessary tables in db
        abstract = True


class Look(TimestampedModel):
    hype        = models.IntegerField('Site hype')
    title       = models.TextField('Look title')
    img_url     = models.URLField('Location of look img')
    desc        = models.TextField('Look description', blank=True)
    orig_id     = models.IntegerField('Original lookbook id')
    orig_hype   = models.IntegerField('Original hype rating')
    location    = models.ForeignKey('Location', related_name='looks')

    def __str__(self):
        return 'Look {id:%s,url:%s}' % (self.orig_id, self.img_url)


class Location(models.Model):
    city    = models.TextField('City', unique=True, blank=True)
    country = models.TextField('Country', unique=True)

    def __str__(self):
        return '{city:%s,country:%s}' % (self.city, self.country)


class Comment(TimestampedModel):
    like = models.IntegerField('Comment Likes')
    body = models.TextField('Comment body', blank=True)
    look = models.ForeignKey(Look, related_name='comments')
