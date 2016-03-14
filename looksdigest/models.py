from django.db import models
from django.utils import timezone


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
    hype        = models.IntegerField('Site hype', default=0)
    title       = models.TextField('Look title', blank=True)
    img_url     = models.URLField('Location of look img')
    desc        = models.TextField('Look description', blank=True)
    orig_id     = models.IntegerField('Original lookbook id', unique=True)
    orig_hype   = models.IntegerField('Original hype rating', default=0)
    orig_date   = models.DateTimeField('Original creation dates', default=timezone.now, blank=True)
    location    = models.ForeignKey('Location', related_name='looks')

    def __str__(self):
        return 'Look %s (%s)' % (self.orig_id, self.img_url)


class Location(models.Model):
    city    = models.CharField('City', max_length=200, null=True)
    country = models.CharField('Country', max_length=200)

    class Meta:
        unique_together = ('city', 'country')

    def __str__(self):
        if self.city is not None:
            return '%s, %s' % (self.city, self.country)
        return '%s' % self.country


class Comment(TimestampedModel):
    like = models.IntegerField('Comment Likes')
    body = models.TextField('Comment body', blank=True)
    look = models.ForeignKey(Look, related_name='comments')
