# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-08 12:37
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0005_auto_20180508_1519'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Editor',
        ),
    ]
