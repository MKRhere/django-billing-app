# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-29 16:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bills', '0004_auto_20170529_2108'),
    ]

    operations = [
        migrations.AddField(
            model_name='bill',
            name='customer_no',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
    ]