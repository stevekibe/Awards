# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-10-21 21:11
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('award', '0003_auto_20181021_2351'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='post',
            new_name='project_img',
        ),
    ]