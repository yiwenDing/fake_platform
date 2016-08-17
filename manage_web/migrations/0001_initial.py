# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-08-08 02:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='fake_item',
            fields=[
                ('id', models.BigIntegerField(max_length=20, primary_key=True, serialize=False)),
                ('api_verison', models.SmallIntegerField(max_length=6)),
                ('cell_item', models.CharField(max_length=128)),
                ('cell_data', models.CharField(max_length=4096)),
                ('description', models.CharField(max_length=64)),
                ('behot_time', models.IntegerField(max_length=11)),
                ('status', models.SmallIntegerField(max_length=6)),
            ],
        ),
        migrations.CreateModel(
            name='item_type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_name', models.CharField(max_length=30)),
                ('items', models.ManyToManyField(to='manage_web.fake_item')),
            ],
        ),
    ]