# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-03-21 13:20
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('line_1', models.CharField(max_length=100)),
                ('line_2', models.CharField(max_length=100)),
                ('line_3', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=50)),
                ('misc_info', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Party',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=250)),
                ('address_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Customer.Address')),
                ('owner_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Customer.Party')),
            ],
        ),
    ]
