# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-08 06:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PitSummary',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Tab', models.CharField(max_length=19)),
                ('Value', models.CharField(blank=True, max_length=20, null=True)),
                ('Pop_Type', models.CharField(max_length=37)),
                ('Shelter', models.CharField(max_length=37)),
                ('Date', models.DateField()),
            ],
        ),
    ]
