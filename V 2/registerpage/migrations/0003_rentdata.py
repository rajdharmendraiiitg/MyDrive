# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-07-09 06:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registerpage', '0002_auto_20170522_1354'),
    ]

    operations = [
        migrations.CreateModel(
            name='RentData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20)),
                ('source', models.CharField(max_length=20)),
                ('destination', models.CharField(max_length=20)),
                ('start', models.CharField(max_length=20)),
                ('end', models.CharField(max_length=20)),
                ('carname', models.CharField(max_length=30)),
                ('ccno', models.CharField(max_length=20)),
                ('cost', models.IntegerField()),
            ],
        ),
    ]
