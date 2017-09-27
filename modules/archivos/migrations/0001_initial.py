# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-06-05 22:41
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('etapas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Archivo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('upload', models.FileField(upload_to='images/')),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('update_time', models.DateTimeField(auto_now=True)),
                ('etata', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='etapas.Etapa')),
            ],
        ),
    ]