from django.db import models

from mentawai.core.utils import FilenameGenerator

from thumbnails.fields import ImageField


class PartnerQuerySet(models.query.QuerySet):

    def is_active(self):
        return self.filter(is_active=True)


class Partner(models.Model):

    name = models.CharField('Nama', max_length=50)
    description = models.TextField('Description', blank=True, null=True)
    photo = ImageField(upload_to=FilenameGenerator(prefix='partner-photo'),
                       default='', blank=True)
    website = models.CharField('Website', max_length=50, blank=True, null=True)
    is_active = models.BooleanField('aktif', default=True)
    objects = models.Manager.from_queryset(PartnerQuerySet)()

    def __unicode__(self):
        return self.name
