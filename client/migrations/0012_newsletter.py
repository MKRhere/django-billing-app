# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-08-02 09:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0011_auto_20170724_1230'),
    ]

    operations = [
        migrations.CreateModel(
            name='Newsletter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.URLField()),
            ],
        ),
    ]
