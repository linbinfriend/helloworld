# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-11 14:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='XXLcolrow',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('MyCloumn', models.IntegerField()),
                ('MyRow', models.IntegerField()),
                ('last_date', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
