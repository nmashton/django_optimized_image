# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-10-13 23:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('not_optimized', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='GenericModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
            ],
        ),
    ]
