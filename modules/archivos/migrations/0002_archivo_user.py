# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-06-05 22:41
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('archivos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='archivo',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]