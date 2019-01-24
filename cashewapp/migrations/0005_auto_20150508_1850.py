# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cashewapp', '0004_auto_20150508_1827'),
    ]

    operations = [
        migrations.RenameField(
            model_name='account',
            old_name='status',
            new_name='active',
        ),
        migrations.RenameField(
            model_name='category',
            old_name='status',
            new_name='active',
        ),
        migrations.AlterField(
            model_name='currency',
            name='long_name',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='keywords',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='note',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='type',
            name='table',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
