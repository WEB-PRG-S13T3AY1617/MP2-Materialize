# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-13 14:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marketplace', '0024_auto_20170813_2200'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offer',
            name='amount',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True),
        ),
    ]
