# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-26 06:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('developersite', '0005_auto_20160725_0826'),
    ]

    operations = [
        migrations.AlterField(
            model_name='developer',
            name='contact',
            field=models.CharField(blank=True, default='', max_length=32, verbose_name='Phone NUmber'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='developer',
            name='g_plus',
            field=models.CharField(blank=True, default='', max_length=32, verbose_name='G+ ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='developer',
            name='profile',
            field=models.ImageField(blank=True, default='', upload_to='uploads', verbose_name='Profile Image'),
            preserve_default=False,
        ),
    ]
