# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-02-06 01:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deals', '0006_auto_20180202_1542'),
    ]

    operations = [
        migrations.AddField(
            model_name='servicedeals',
            name='deleted',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='servicedeals',
            name='deleted_at',
            field=models.DateTimeField(blank=True, default=None, null=True),
        ),
    ]
