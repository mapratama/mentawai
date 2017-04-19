from django.db import models

from mentawai.core.utils import FilenameGenerator

from thumbnails.fields import ImageField


class NewsQuerySet(models.query.QuerySet):

    def is_active(self):
        return self.filter(is_active=True)


class News(models.Model):

    title = models.CharField('Judul', max_length=50)
    content = models.TextField('Isi Berita', blank=True, null=True)
    photo = ImageField(upload_to=FilenameGenerator(prefix='news-photo'),
                       default='', blank=True)
    is_active = models.BooleanField('aktif', default=True)
    objects = models.Manager.from_queryset(NewsQuerySet)()

    def __unicode__(self):
        return self.title
