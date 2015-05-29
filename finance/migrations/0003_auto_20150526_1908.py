# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('finance', '0002_auto_20150526_1127'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='vatcode',
            options={'verbose_name': 'VAT code'},
        ),
    ]
