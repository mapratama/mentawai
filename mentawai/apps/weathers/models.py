from django.db import models

from django.core.validators import MinValueValidator

from django.utils import timezone

from model_utils import Choices


class WeatherQuerySet(models.query.QuerySet):

    def is_future(self):
        return self.filter(date__gte=timezone.now())


class Weather(models.Model):

    date = models.DateField('Tanggal')
    description = models.TextField('Deskripsi', blank=True, null=True)
    temperature = models.CharField('Suhu', max_length=50)
    humidity = models.CharField('Kelembaban', max_length=50)
    wind_velocity = models.PositiveIntegerField('Kecepatan Angin',
                                                validators=[MinValueValidator(0)])

    WIND_DIRECTION = Choices(
        (1, 'utara', 'Utara'),
        (2, 'timur_laut', 'Timur Laut'),
        (3, 'timur', 'Timur'),
        (4, 'tenggara', 'Tenggara'),
        (5, 'selatan', 'Selatan'),
        (6, 'barat_daya', 'Barat Daya'),
        (7, 'barat', 'Barat'),
        (8, 'barat_laut', 'Barat Laut'),
    )

    wind_direction = models.PositiveSmallIntegerField('Arah Angin', choices=WIND_DIRECTION)
    objects = models.Manager.from_queryset(WeatherQuerySet)()

    def __unicode__(self):
        return self.date
