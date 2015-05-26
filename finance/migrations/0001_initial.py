# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import finance.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='VatCode',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('slug', models.SlugField(max_length=10)),
                ('description', models.CharField(max_length=100)),
                ('rate', models.DecimalField(decimal_places=3, max_digits=5)),
                ('deleted', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='VatSettings',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('vat_number', models.CharField(max_length=12, blank=True)),
                ('standard_vat_code', models.ForeignKey(to='finance.VatCode', default=finance.models.default_vat_code, related_name='+')),
            ],
            options={
                'verbose_name': 'VAT settings',
            },
        ),
    ]
