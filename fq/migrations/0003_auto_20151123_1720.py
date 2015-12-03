# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fq', '0002_auto_20151123_1633'),
    ]

    operations = [
        migrations.AlterField(
            model_name='venues',
            name='address',
            field=models.CharField(blank=True, max_length=45, null=True),
        ),
        migrations.AlterField(
            model_name='venues',
            name='city',
            field=models.CharField(blank=True, max_length=45, null=True),
        ),
    ]
