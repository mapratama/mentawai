from django.db import models

from mentawai.core.utils import FilenameGenerator

from model_utils import Choices
from thumbnails.fields import ImageField


class WaveQuerySet(models.query.QuerySet):

    def is_active(self):
        return self.filter(is_active=True)


class Wave(models.Model):

    name = models.CharField('Nama', max_length=50)
    TYPE = Choices(
        (1, 'kiri', 'Kiri'),
        (2, 'kanan', 'Kanan'),
        (3, 'kiri_kanan', 'Kiri dan Kanan'),
    )

    type = models.PositiveSmallIntegerField('Tipe', choices=TYPE)
    lat = models.FloatField()
    long = models.FloatField()
    location = models.ForeignKey('locations.Location', related_name='waves')
    address = models.TextField('Alamat', blank=True, null=True)
    is_active = models.BooleanField('aktif', default=True)
    photo = ImageField(upload_to=FilenameGenerator(prefix='wave-photo'),
                       default='', blank=True)
    objects = models.Manager.from_queryset(WaveQuerySet)()

    def __unicode__(self):
        return self.name
