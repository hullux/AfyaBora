# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-11-03 18:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0004_auto_20171103_1847'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patientmedicaldata',
            name='used_arv',
            field=models.CharField(choices=[('Yes', 'YES'), ('No', 'NO')], default='No', max_length=5),
        ),
    ]