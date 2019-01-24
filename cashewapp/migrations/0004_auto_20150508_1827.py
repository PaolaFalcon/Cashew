# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cashewapp', '0003_auto_20150508_1753'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'categories'},
        ),
        migrations.AlterModelOptions(
            name='currency',
            options={'verbose_name_plural': 'currencies'},
        ),
        migrations.AlterField(
            model_name='category',
            name='parent',
            field=models.ForeignKey(default=None, blank=True, to='cashewapp.Category', null=True),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='category',
            field=models.ForeignKey(default=None, blank=True, to='cashewapp.Category', null=True),
        ),
    ]
