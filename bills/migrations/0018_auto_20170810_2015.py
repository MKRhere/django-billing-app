# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-08-10 14:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bills', '0017_remove_bill_customer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='quantity',
            field=models.PositiveIntegerField(default=1),
        ),
    ]
