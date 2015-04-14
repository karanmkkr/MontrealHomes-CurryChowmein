# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useraddress',
            name='state',
            field=models.CharField(blank=True, max_length=120, null=True, choices=[(b'AB', 'Alberta'), (b'BC', 'British Columbia'), (b'MB', 'Manitoba'), (b'NB', 'New Brunswick'), (b'NL', 'Newfoundland and Labrador'), (b'NT', 'Northwest Territories'), (b'NS', 'Nova Scotia'), (b'NU', 'Nunavut'), (b'ON', 'Ontario'), (b'PE', 'Prince Edward Island'), (b'QC', 'Quebec'), (b'SK', 'Saskatchewan'), (b'YT', 'Yukon')]),
            preserve_default=True,
        ),
    ]
