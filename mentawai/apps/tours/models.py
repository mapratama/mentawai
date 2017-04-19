from django.db import models

from mentawai.core.utils import FilenameGenerator

from model_utils import Choices
from thumbnails.fields import ImageField


class TourQuerySet(models.query.QuerySet):

    def is_active(self):
        return self.filter(is_active=True)


class Tour(models.Model):

    name = models.CharField('Nama', max_length=50)
    location = models.ForeignKey('locations.Location', related_name='tours')
    TYPE = Choices(
        (1, 'alam', 'Alam'),
        (2, 'pantai', 'Pantai'),
        (3, 'panaorama', 'Panorama'),
        (4, 'budaya', 'Budaya'),
        (5, 'diving', 'Diving'),
        (6, 'snorkeling', 'Snorkeling'),
        (7, 'memancing', 'Memancing'),
        (8, 'hutan', 'Hutan'),
    )

    type = models.PositiveSmallIntegerField('Tipe', choices=TYPE)
    description = models.TextField('Description', blank=True, null=True)
    address = models.TextField('Alamat', blank=True, null=True)
    lat = models.FloatField(blank=True, null=True)
    long = models.FloatField(blank=True, null=True)
    photo = ImageField(upload_to=FilenameGenerator(prefix='tour-photo'),
                       default='', blank=True)
    is_active = models.BooleanField('aktif', default=True)
    objects = models.Manager.from_queryset(TourQuerySet)()

    def __unicode__(self):
        return self.name
