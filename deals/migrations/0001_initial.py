# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-01-31 18:33
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('services', '0004_auto_20180130_2041'),
        ('companies', '0030_auto_20180126_0903'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Deals',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('closed', models.BooleanField(default=False, help_text='Tells if a deal is closed or open', verbose_name='Closed Deal')),
                ('prospect', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('seller', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='companies.Affiliates')),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='services.Services')),
            ],
        ),
    ]
