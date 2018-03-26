# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-03-14 08:43
from __future__ import unicode_literals

import courseManagement.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='parCatUUID',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuidNumber', models.BigIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='parentCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('courseCategoryId', models.CharField(default=courseManagement.models.getparentCategoryId, max_length=200, unique=True)),
                ('parentCategoryId', models.TextField(blank=True, null=True)),
                ('categoryName', models.TextField(blank=True, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('createdDate', models.DateTimeField(auto_now_add=True)),
                ('modifiedDate', models.DateTimeField(auto_now=True)),
                ('isActive', models.BooleanField(default=True)),
                ('createdBy', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='parentCategoryCreatedBy', to=settings.AUTH_USER_MODEL)),
                ('modifiedBy', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='parentCategoryModifiedBy', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]