# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-23 22:23
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
            name='Seguido',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Useguido', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Usuario_seguido', to=settings.AUTH_USER_MODEL)),
                ('Useguidor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Usuario_que_sigue', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
