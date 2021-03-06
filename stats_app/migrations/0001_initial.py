# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-11 20:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CityStats',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', models.CharField(db_index=True, max_length=64, verbose_name='State')),
                ('city', models.CharField(db_index=True, max_length=64, verbose_name='City')),
                ('quantity', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='UserStats',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(db_index=True, max_length=64, verbose_name='User')),
                ('quantity', models.IntegerField()),
            ],
        ),
    ]
