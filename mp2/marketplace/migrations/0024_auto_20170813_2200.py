# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-13 14:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marketplace', '0023_auto_20170813_2134'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offer',
            name='secondhand',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]