# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-07-22 03:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('developersite', '0002_auto_20160722_0301'),
    ]

    operations = [
        migrations.AlterField(
            model_name='developer',
            name='profile',
            field=models.ImageField(blank=True, null=True, upload_to=b''),
        ),
    ]
