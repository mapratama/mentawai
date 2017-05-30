from django.db import models


class Content(models.Model):

    photos = models.ManyToManyField('photos.photo', related_name='contents')
    name = models.CharField(max_length=50)
    key = models.CharField(max_length=30, unique=True)
    description = models.TextField()

    def __unicode__(self):
        return self.name
