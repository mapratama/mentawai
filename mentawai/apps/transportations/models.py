from django.db import models

from mentawai.core.utils import FilenameGenerator

from model_utils import Choices
from thumbnails.fields import ImageField


class TransportationQuerySet(models.query.QuerySet):

    def is_active(self):
        return self.filter(is_active=True)


class Transportation(models.Model):

    name = models.CharField('Nama', max_length=50)
    TYPE = Choices(
        (1, 'kapal_feri', 'Kapal Feri'),
        (2, 'pesawat', 'Pesawat'),
    )

    type = models.PositiveSmallIntegerField('Tipe', choices=TYPE)

    DAY = Choices(
        (0, 'senin', 'Senin'),
        (1, 'selasa', 'Selasa'),
        (2, 'rabu', 'Rabu'),
        (3, 'kamis', 'Kamis'),
        (4, 'jumat', 'Jumat'),
        (5, 'sabtu', 'Sabtu'),
        (6, 'minggu', 'Minggu'),
    )
    day = models.PositiveSmallIntegerField(choices=DAY)

    photo = ImageField(upload_to=FilenameGenerator(prefix='transportation-photo'),
                       default='', blank=True)

    departure_time = models.TimeField('Waktu Keberangkatan', blank=True, null=True)
    arrived_time = models.TimeField('Waktu Tiba', blank=True, null=True)
    pickup_location = models.CharField('Asal', max_length=50)
    destination = models.CharField('Tujuan', max_length=50)
    is_active = models.BooleanField('aktif', default=True)
    objects = models.Manager.from_queryset(TransportationQuerySet)()

    def __unicode__(self):
        return self.name
