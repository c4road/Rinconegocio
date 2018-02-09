# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-01-13 05:18
from __future__ import unicode_literals

import companies.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0015_auto_20180112_2133'),
    ]

    operations = [
        migrations.AddField(
            model_name='affiliates',
            name='lead_magnet',
            field=models.FileField(blank=True, null=True, upload_to=companies.models.upload_file_to),
        ),
    ]
