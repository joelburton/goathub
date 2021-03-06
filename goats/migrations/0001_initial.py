# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-14 00:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Goat',
            fields=[
                ('name', models.CharField(max_length=50, unique=True)),
                ('slug', models.SlugField(max_length=20, primary_key=True, serialize=False)),
                ('description', models.TextField(blank=True)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
    ]
