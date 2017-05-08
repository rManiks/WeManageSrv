# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-06 12:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Customer', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='address',
            name='geo_location',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='address',
            name='misc_info',
            field=models.CharField(default='', max_length=200),
        ),
    ]
