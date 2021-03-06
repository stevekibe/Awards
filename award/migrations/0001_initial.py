# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-10-18 12:16
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Detail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', tinymce.models.HTMLField()),
                ('user_image', models.ImageField(upload_to='images/')),
                ('user', models.OneToOneField(null='True', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post', models.ImageField(blank=True, upload_to='images/')),
                ('project_detail', tinymce.models.HTMLField()),
                ('link', tinymce.models.HTMLField()),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
                ('detail', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='award.Detail')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['pub_date'],
            },
        ),
    ]
