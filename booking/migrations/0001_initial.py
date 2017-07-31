# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-15 06:35
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vehicle_type', models.CharField(choices=[('Bus', 'Bus'), ('Taxi', 'Taxi'), ('Micro', 'Micro'), ('Tempo', 'Tempo')], max_length=50)),
                ('vehicle_name', models.CharField(max_length=50, null=True)),
                ('source', models.CharField(max_length=50)),
                ('destination', models.CharField(max_length=50)),
                ('booking_on', models.DateTimeField(auto_now_add=True)),
                ('booked', models.BooleanField(default=False)),
                ('booking_for', models.DateTimeField(null=True)),
                ('occupancy', models.IntegerField(null=True)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]