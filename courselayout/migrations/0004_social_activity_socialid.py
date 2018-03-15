# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-15 05:46
from __future__ import unicode_literals

import courselayout.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('courselayout', '0003_single_activity_singleid'),
    ]

    operations = [
        migrations.CreateModel(
            name='social_activity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('soid', models.CharField(default=courselayout.models.getsocialid, max_length=200, unique=True)),
                ('noofsessions', models.IntegerField()),
                ('courseId', models.TextField(blank=True, null=True)),
                ('isActive', models.BooleanField(default=True)),
                ('createdDate', models.DateTimeField(auto_now_add=True)),
                ('modifiedDate', models.DateTimeField(auto_now=True)),
                ('createdBy', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='socialactivityCreatedBy', to=settings.AUTH_USER_MODEL)),
                ('modifiedBy', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='socialactivityModifiedBy', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='socialID',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuidNumber', models.BigIntegerField(default=0)),
            ],
        ),
    ]
