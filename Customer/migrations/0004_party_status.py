# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-26 11:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Customer', '0003_party_avatar'),
    ]

    operations = [
        migrations.AddField(
            model_name='party',
            name='status',
            field=models.CharField(default='ACTIVE', max_length=10),
        ),
    ]
