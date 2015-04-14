# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContactUs',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=120, null=True, blank=True)),
                ('email', models.EmailField(max_length=300)),
                ('message', models.CharField(max_length=400)),
                ('timestamp', models.DateTimeField(default=datetime.datetime(2015, 4, 7, 9, 41, 46, 10422), auto_now_add=True)),
            ],
            options={
                'ordering': ['-timestamp'],
            },
            bases=(models.Model,),
        ),
    ]
