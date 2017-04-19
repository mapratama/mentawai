from django.db import models


class Location(models.Model):

    name = models.CharField('Nama', max_length=50)

    def __unicode__(self):
        return self.name
