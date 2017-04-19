# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2017-04-16 16:29
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Weather',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name=b'Tanggal')),
                ('description', models.TextField(blank=True, null=True, verbose_name=b'Deskripsi')),
                ('temperature', models.CharField(max_length=50, verbose_name=b'Suhu')),
                ('humidity', models.CharField(max_length=50, verbose_name=b'Kelembaban')),
                ('wind_velocity', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(0)], verbose_name=b'Kecepatan Angin')),
                ('wind_direction', models.PositiveSmallIntegerField(choices=[(1, b'Utara'), (2, b'Timur Laut'), (3, b'Timur'), (4, b'Tenggara'), (5, b'Selatan'), (6, b'Barat Daya'), (7, b'Barat'), (8, b'Barat Laut')], verbose_name=b'Arah Angin')),
            ],
        ),
    ]
