# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-13 13:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marketplace', '0022_auto_20170808_1932'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offer',
            name='secondhand',
            field=models.IntegerField(blank=True),
        ),
    ]