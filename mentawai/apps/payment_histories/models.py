from django.db import models

from model_utils import Choices
from model_utils.fields import AutoCreatedField


class PaymentHistory(models.Model):
    user = models.ForeignKey('users.User', related_name='payment_histories')
    STATUS = Choices(
        (1, 'new', 'New'),
        (2, 'completed', 'Completed'),
        (3, 'failed', 'Failed'),
    )
    status = models.PositiveSmallIntegerField(choices=STATUS, default=STATUS.new)
    value = models.FloatField()
    created = AutoCreatedField()
    payment_id = models.CharField(max_length=255, default='')
    error_log = models.TextField(default='', blank=True)

    def __unicode__(self):
        return "%s (%s)" % (self.user, self.payment_id)
