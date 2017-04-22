from django.db import models

from mentawai.core.utils import FilenameGenerator

from model_utils import Choices
from thumbnails.fields import ImageField


class ResortQuerySet(models.query.QuerySet):

    def is_active(self):
        return self.filter(is_active=True)


class Resort(models.Model):

    name = models.CharField('Nama', max_length=50)
    TYPE = Choices(
        (1, 'resort', 'Resort'),
        (2, 'penginapan', 'Penginapan'),
    )

    type = models.PositiveSmallIntegerField('Tipe', choices=TYPE)
    location = models.ForeignKey('locations.Location', related_name='resorts')
    address = models.TextField('Alamat', blank=True, null=True)
    photo = ImageField(upload_to=FilenameGenerator(prefix='resort-photo'),
                       default='', blank=True)
    website = models.CharField(max_length=50, blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    lat = models.FloatField(blank=True, null=True)
    long = models.FloatField(blank=True, null=True)
    is_active = models.BooleanField('aktif', default=True)
    objects = models.Manager.from_queryset(ResortQuerySet)()

    def __unicode__(self):
        return self.name
