# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-09-26 14:09
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Admin_login',
            fields=[
                ('sir_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('email_address', models.EmailField(max_length=254, primary_key=True, serialize=False)),
                ('Login_time', models.DateTimeField(auto_now=True)),
                ('pswd', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Bio_data',
            fields=[
                ('patient_no', models.IntegerField(default=1, primary_key=True, serialize=False)),
                ('sir_name', models.CharField(default='', max_length=30)),
                ('first_name', models.CharField(default='', max_length=30)),
                ('second_name', models.CharField(default='', max_length=30)),
                ('DOB', models.DateTimeField(blank=True, null=True)),
                ('phone_no', models.IntegerField()),
                ('id_no', models.IntegerField()),
                ('age', models.IntegerField(blank=True, null=True)),
                ('NoK', models.CharField(blank=True, max_length=30, null=True)),
                ('physical_address', models.CharField(max_length=30)),
            ],
            options={
                'ordering': ['sir_name'],
            },
        ),
        migrations.CreateModel(
            name='Clinician_details',
            fields=[
                ('sir_name', models.CharField(max_length=30)),
                ('first_name', models.CharField(max_length=30)),
                ('second_name', models.CharField(max_length=30)),
                ('job_number', models.IntegerField(primary_key=True, serialize=False)),
                ('facility', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Clinician_login',
            fields=[
                ('sir_name', models.CharField(max_length=30)),
                ('second_name', models.CharField(max_length=30)),
                ('email_address', models.EmailField(max_length=254, primary_key=True, serialize=False)),
                ('pswd', models.CharField(max_length=30)),
                ('job_number', models.IntegerField()),
                ('last_login_time', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['sir_name'],
            },
        ),
        migrations.CreateModel(
            name='Medical_data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patient_no', models.IntegerField(default=1)),
                ('date_confirmed', models.DateField()),
                ('date_enrolled', models.DateField()),
                ('used_arv', models.CharField(default='None', max_length=20)),
                ('spouse', models.CharField(blank=True, default='None', max_length=40, null=True)),
                ('known_allergies', models.CharField(blank=True, max_length=500, null=True)),
                ('entry_point', models.CharField(default='None', max_length=30)),
                ('CD4_count', models.IntegerField(blank=True, default=0, null=True)),
                ('DLD', models.CharField(default='', max_length=50)),
            ],
            options={
                'ordering': ['patient_no'],
            },
        ),
        migrations.CreateModel(
            name='Next_of_Kin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(default='', max_length=30)),
                ('phone_no', models.IntegerField()),
                ('relationship', models.CharField(default='None', max_length=40)),
                ('sir_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.Bio_data')),
            ],
            options={
                'ordering': ['sir_name'],
            },
        ),
        migrations.CreateModel(
            name='Transfer_in',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patient_no', models.IntegerField(default=1)),
                ('sir_name', models.CharField(max_length=30)),
                ('first_name', models.CharField(max_length=30)),
                ('second_name', models.CharField(max_length=30)),
                ('DOB', models.DateField()),
                ('date_coming', models.DateField()),
                ('facility_from', models.CharField(max_length=50)),
                ('date_confirmed', models.DateField()),
                ('date_enrolled', models.DateField()),
                ('date_started_ART', models.DateField()),
            ],
            options={
                'ordering': ['date_coming'],
            },
        ),
        migrations.CreateModel(
            name='Visit_details',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sir_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('visit_date', models.DateField()),
                ('refilled', models.CharField(max_length=30)),
                ('tests_done', models.CharField(max_length=500)),
                ('comments', models.CharField(max_length=500)),
                ('patient_no', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='dashboard.Medical_data')),
            ],
        ),
    ]
