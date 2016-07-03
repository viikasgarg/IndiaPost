# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-03 08:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PostalCode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('officename', models.CharField(blank=True, max_length=100, null=True, verbose_name='Officename')),
                ('pincode', models.CharField(blank=True, max_length=100, null=True, unique=True, verbose_name='pincode')),
                ('officeType', models.CharField(blank=True, max_length=100, null=True, verbose_name='officeType')),
                ('deliverystatus', models.CharField(blank=True, max_length=100, null=True, verbose_name='Deliverystatus')),
                ('divisionname', models.CharField(blank=True, max_length=100, null=True, verbose_name='divisionname')),
                ('region_name', models.CharField(blank=True, max_length=100, null=True, verbose_name='Region name')),
                ('circlename', models.CharField(blank=True, max_length=100, null=True, verbose_name='Circlename')),
                ('taluk', models.CharField(blank=True, max_length=100, null=True, verbose_name='Taluk')),
                ('districtname', models.CharField(blank=True, max_length=100, null=True, verbose_name='Districtname')),
                ('state_name', models.CharField(blank=True, max_length=100, null=True, verbose_name='State name')),
                ('pricing_code', models.CharField(blank=True, max_length=100, null=True, verbose_name='Pricing Code')),
            ],
        ),
    ]