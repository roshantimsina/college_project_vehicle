# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-04-25 11:21
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vehicle', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Route',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('source', models.CharField(max_length=50)),
                ('destination', models.CharField(max_length=50)),
                ('fare', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vechile_type', models.CharField(choices=[('Bus', 'Bus'), ('Taxi', 'Taxi'), ('Micro', 'Micro'), ('Tempo', 'Tempo')], max_length=200)),
                ('vechile_number', models.IntegerField(blank=True, null=True)),
                ('contact_number', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='TaxiDriver',
        ),
        migrations.DeleteModel(
            name='TaxiZone',
        ),
        migrations.DeleteModel(
            name='VehicleZone',
        ),
        migrations.AddField(
            model_name='route',
            name='vechile_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vehicle.Vehicle'),
        ),
    ]
