# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2017-04-20 13:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20170419_1833'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(db_index=True, max_length=254, null=True, unique=True),
        ),
    ]
