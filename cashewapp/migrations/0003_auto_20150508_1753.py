# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cashewapp', '0002_category_parent_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='account',
            old_name='currency_id',
            new_name='currency',
        ),
        migrations.RenameField(
            model_name='account',
            old_name='type_id',
            new_name='type',
        ),
        migrations.RenameField(
            model_name='transaction',
            old_name='account_id',
            new_name='account',
        ),
        migrations.RemoveField(
            model_name='category',
            name='parent_id',
        ),
        migrations.RemoveField(
            model_name='transaction',
            name='category_id',
        ),
        migrations.AddField(
            model_name='category',
            name='parent',
            field=models.ForeignKey(default=None, to='cashewapp.Category', null=True),
        ),
        migrations.AddField(
            model_name='transaction',
            name='category',
            field=models.ForeignKey(default=None, to='cashewapp.Category', null=True),
        ),
    ]
