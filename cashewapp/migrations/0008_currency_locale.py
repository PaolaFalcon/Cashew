# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cashewapp', '0007_auto_20150529_1158'),
    ]

    operations = [
        migrations.AddField(
            model_name='currency',
            name='locale',
            field=models.CharField(default=b'en_US', max_length=5),
        ),
    ]
