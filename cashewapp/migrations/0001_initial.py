# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('status', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('status', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Currency',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('long_name', models.CharField(max_length=200)),
                ('short_name', models.CharField(max_length=3)),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('keywords', models.CharField(max_length=200)),
                ('date', models.DateField()),
                ('note', models.CharField(max_length=1000)),
                ('amount', models.DecimalField(max_digits=19, decimal_places=2)),
                ('account_id', models.ForeignKey(to='cashewapp.Account')),
                ('category_id', models.ForeignKey(to='cashewapp.Category')),
            ],
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('table', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='account',
            name='currency_id',
            field=models.ForeignKey(to='cashewapp.Currency'),
        ),
        migrations.AddField(
            model_name='account',
            name='type_id',
            field=models.ForeignKey(to='cashewapp.Type'),
        ),
    ]
