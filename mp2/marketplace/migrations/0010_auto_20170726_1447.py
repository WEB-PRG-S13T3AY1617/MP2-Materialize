# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-26 06:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marketplace', '0009_auto_20170726_1445'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, default='marketplace/static/marketplace/img/def/default.png', upload_to='marketplace/static/marketplace/img/'),
        ),
    ]