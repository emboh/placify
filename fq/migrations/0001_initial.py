# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cities',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('city', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Regions',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('region', models.CharField(max_length=20)),
                ('cities_id', models.ForeignKey(to='fq.Cities')),
            ],
        ),
        migrations.CreateModel(
            name='Texts',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('word', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Tips',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('text', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Venues',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=45)),
                ('address', models.CharField(max_length=45)),
                ('city', models.CharField(max_length=45)),
                ('lat', models.FloatField()),
                ('lng', models.FloatField()),
                ('regions_id', models.ForeignKey(to='fq.Regions')),
            ],
        ),
        migrations.AddField(
            model_name='tips',
            name='venues_id',
            field=models.ForeignKey(to='fq.Venues'),
        ),
        migrations.AddField(
            model_name='texts',
            name='tips_id',
            field=models.ForeignKey(to='fq.Tips'),
        ),
    ]
