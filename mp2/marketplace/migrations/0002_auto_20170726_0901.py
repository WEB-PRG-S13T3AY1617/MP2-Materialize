# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-26 01:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marketplace', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='degree_office',
            new_name='first_name',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='firstname',
            new_name='last_name',
        ),
        migrations.RemoveField(
            model_name='post',
            name='academic',
        ),
        migrations.RemoveField(
            model_name='user',
            name='lastname',
        ),
        migrations.AddField(
            model_name='post',
            name='academic_or_office',
            field=models.CharField(choices=[('1', 'Academic'), ('2', 'Office')], default='1', max_length=1),
        ),
        migrations.AddField(
            model_name='user',
            name='degree_or_office',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AlterField(
            model_name='post',
            name='course',
            field=models.CharField(default=0, max_length=20),
        ),
    ]
