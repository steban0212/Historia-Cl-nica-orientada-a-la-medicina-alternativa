# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-03-08 03:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Historiaclinica', '0024_auto_20180306_2324'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='plan_manejo',
            name='id_paciente',
        ),
        migrations.RemoveField(
            model_name='resultado_examen',
            name='id_paciente',
        ),
        migrations.RemoveField(
            model_name='terapias',
            name='Especificaciones',
        ),
        migrations.RemoveField(
            model_name='terapias',
            name='Estado',
        ),
        migrations.RemoveField(
            model_name='terapias',
            name='Terapia',
        ),
        migrations.AddField(
            model_name='terapias',
            name='Plan_terapeutico',
            field=models.CharField(default=1, max_length=800),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Plan_manejo',
        ),
        migrations.DeleteModel(
            name='Resultado_Examen',
        ),
    ]
