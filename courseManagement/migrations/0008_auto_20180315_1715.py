# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-03-15 11:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courseManagement', '0007_auto_20180314_1608'),
    ]

    operations = [
        migrations.AlterField(
            model_name='parentcategory',
            name='createdBy',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='parentcategory',
            name='modifiedBy',
            field=models.TextField(blank=True, null=True),
        ),
    ]