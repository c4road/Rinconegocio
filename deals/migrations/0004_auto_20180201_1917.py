# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-02-01 23:17
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('deals', '0003_auto_20180131_1615'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicedeals',
            name='service',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='services.Services'),
        ),
    ]