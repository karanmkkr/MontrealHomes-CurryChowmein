# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0013_auto_20150413_2209'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactus',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 14, 7, 43, 18, 302108), auto_now_add=True),
            preserve_default=True,
        ),
    ]
