from django.db import models

from thumbnails.fields import ImageField

from mentawai.core.utils import FilenameGenerator


class Photo(models.Model):

    photo = ImageField(upload_to=FilenameGenerator(prefix='photo'),
                       default='', blank=True)
    name = models.CharField(max_length=255)

    def __unicode__(self):
        return self.name
