# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-02-04 17:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0007_auto_20180204_1312'),
    ]

    operations = [
        migrations.AlterField(
            model_name='services',
            name='en_name',
            field=models.CharField(blank=True, default='', max_length=50, null=True, verbose_name='English Title'),
        ),
    ]
