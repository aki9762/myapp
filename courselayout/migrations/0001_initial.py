# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-14 11:19
from __future__ import unicode_literals

import courselayout.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='format_type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fId', models.CharField(default=courselayout.models.getgroupId, max_length=200, unique=True)),
                ('name', models.TextField(blank=True, null=True)),
                ('isActive', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='groupUUID',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuidNumber', models.BigIntegerField(default=0)),
            ],
        ),
    ]
