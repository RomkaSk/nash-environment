# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-01-04 07:41
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0005_result'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ExcelFile',
            new_name='InputFile',
        ),
    ]