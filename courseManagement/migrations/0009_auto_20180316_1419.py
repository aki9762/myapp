# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-03-16 08:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courseManagement', '0008_auto_20180315_1715'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='ModifiedBy',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='createdBy',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='courselayout',
            name='createdBy',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='courselayout',
            name='modifiedBy',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='filesupload',
            name='createdBy',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='filesupload',
            name='modifiedBy',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='forcelanguage',
            name='createdBy',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='forcelanguage',
            name='modifiedBy',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='formattbl',
            name='createdBy',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='formattbl',
            name='modifiedBy',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='hiddensection',
            name='createdBy',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='hiddensection',
            name='modifiedBy',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='yesno',
            name='createdBy',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='yesno',
            name='modifiedBy',
            field=models.TextField(blank=True, null=True),
        ),
    ]
