# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-10-13 14:10
from __future__ import unicode_literals

from django.db import migrations
import django.db.models.deletion
import mptt.fields


class Migration(migrations.Migration):

    dependencies = [
        ('rating', '0006_auto_20161005_1520'),
    ]

    operations = [
        migrations.AddField(
            model_name='location',
            name='parent',
            field=mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='rating.Location'),
        ),
    ]
