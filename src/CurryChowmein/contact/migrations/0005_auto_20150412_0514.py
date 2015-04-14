# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0004_auto_20150407_1207'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactus',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 12, 5, 14, 26, 309789), auto_now_add=True),
            preserve_default=True,
        ),
    ]
