# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0012_auto_20150413_0755'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactus',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 13, 22, 9, 56, 819533), auto_now_add=True),
            preserve_default=True,
        ),
    ]
