# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-21 15:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=15)),
                ('lastname', models.CharField(max_length=15)),
                ('email', models.CharField(max_length=30, unique=True)),
                ('address', models.CharField(max_length=30)),
                ('username', models.CharField(max_length=10, unique=True)),
                ('password', models.CharField(max_length=15, unique=True)),
                ('creditcard', models.CharField(max_length=15, unique=True)),
                ('expiredate', models.CharField(max_length=10)),
            ],
        ),
    ]
