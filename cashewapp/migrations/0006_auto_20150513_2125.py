# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cashewapp', '0005_auto_20150508_1850'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='keywords',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='note',
            field=models.CharField(max_length=1000, null=True, blank=True),
        ),
    ]
