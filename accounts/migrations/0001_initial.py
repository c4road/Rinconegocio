# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-01-28 15:59
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone
import django_countries.fields
import languages.fields
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0008_alter_user_username_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('email', models.EmailField(max_length=255, unique=True, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('name', models.CharField(max_length=255, verbose_name='name')),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True)),
                ('first_name', models.CharField(blank=True, default=None, max_length=50, null=True, verbose_name='First name')),
                ('last_name', models.CharField(blank=True, default=None, max_length=50, null=True, verbose_name='Last name')),
                ('language', languages.fields.LanguageField(blank=True, choices=[('en', 'English'), ('es', 'Spanish')], default=None, max_length=3, null=True, verbose_name='Prefered language')),
                ('country', django_countries.fields.CountryField(blank=True, default=None, max_length=2, null=True, verbose_name='Country')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'ordering': ['name', 'email'],
                'abstract': False,
            },
        ),
    ]