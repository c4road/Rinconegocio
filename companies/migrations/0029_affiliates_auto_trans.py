# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-01-21 18:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0028_auto_20180120_2108'),
    ]

    operations = [
        migrations.AddField(
            model_name='affiliates',
            name='auto_trans',
            field=models.BooleanField(default=False, help_text='Create automatic translation of description. You can edit it later in update page', verbose_name='Automatic Translation'),
        ),
    ]
