# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-06-23 19:33
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('useraccount', '0011_auto_20180623_1933'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bird_hit_form',
            name='time_of_occ',
            field=models.TimeField(default=datetime.datetime(2018, 6, 23, 19, 33, 38, 813830), verbose_name='time published'),
        ),
        migrations.AlterField(
            model_name='bird_hit_form',
            name='time_stamp',
            field=models.DateTimeField(default=datetime.datetime(2018, 6, 23, 19, 33, 38, 813503, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='incident_form',
            name='time_of_incident',
            field=models.TimeField(default=datetime.datetime(2018, 6, 23, 19, 33, 38, 815554), verbose_name='time published'),
        ),
        migrations.AlterField(
            model_name='incident_form',
            name='time_stamp',
            field=models.DateTimeField(default=datetime.datetime(2018, 6, 23, 19, 33, 38, 815425, tzinfo=utc)),
        ),
    ]
