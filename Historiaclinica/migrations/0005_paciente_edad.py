# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-13 01:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Historiaclinica', '0004_usuario'),
    ]

    operations = [
        migrations.AddField(
            model_name='paciente',
            name='Edad',
            field=models.IntegerField(default=2),
            preserve_default=False,
        ),
    ]
