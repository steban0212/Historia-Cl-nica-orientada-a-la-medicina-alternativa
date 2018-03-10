# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-03-02 04:52
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Historiaclinica', '0021_auto_20180302_0348'),
    ]

    operations = [
        migrations.CreateModel(
            name='Antec_fami',
            fields=[
                ('Id_Familiar', models.AutoField(max_length=35, primary_key=True, serialize=False, unique=True)),
                ('Antec_fami', models.CharField(max_length=800)),
                ('id_paciente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Historiaclinica.paciente')),
            ],
        ),
        migrations.AlterField(
            model_name='rev_sistemas',
            name='Rev_consulta',
            field=models.CharField(max_length=800),
        ),
    ]