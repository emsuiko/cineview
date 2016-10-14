# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-10-13 14:40
from __future__ import unicode_literals

from django.db import migrations
import django.db.models.deletion
import mptt.fields


class Migration(migrations.Migration):

    dependencies = [
        ('rating', '0013_row_seat_count'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cinema',
            name='parent',
            field=mptt.fields.TreeForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cinema', to='rating.Location', verbose_name='Location'),
        ),
        migrations.AlterField(
            model_name='hall',
            name='parent',
            field=mptt.fields.TreeForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='halls', to='rating.Cinema', verbose_name='Cinema'),
        ),
        migrations.AlterField(
            model_name='row',
            name='parent',
            field=mptt.fields.TreeForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rows', to='rating.Hall', verbose_name='Hall'),
        ),
        migrations.AlterField(
            model_name='seat',
            name='parent',
            field=mptt.fields.TreeForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='seats', to='rating.Row', verbose_name='Row'),
        ),
    ]
