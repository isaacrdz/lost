# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-04 21:59
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('persons', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='timestamp',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
