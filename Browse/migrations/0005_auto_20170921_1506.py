# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-21 15:06
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Browse', '0004_auto_20170921_1505'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='items',
            name='item_logo',
        ),
        migrations.AlterField(
            model_name='expired',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2017, 9, 21, 15, 6, 25, 134393, tzinfo=utc)),
        ),
    ]
