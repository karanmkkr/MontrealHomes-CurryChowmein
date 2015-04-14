# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('joins', '0003_auto_20150414_0743'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='join',
            unique_together=set([]),
        ),
        migrations.RemoveField(
            model_name='join',
            name='ref_id',
        ),
    ]
