# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-04 22:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('persons', '0003_auto_20160704_2204'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
