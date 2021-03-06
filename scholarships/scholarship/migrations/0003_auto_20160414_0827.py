# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-04-14 08:27
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('scholarship', '0002_auto_20160414_0618'),
    ]

    operations = [
        migrations.CreateModel(
            name='profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('GN', 'General'), ('OBC', 'OBC'), ('SC/ST', 'SC/ST')], max_length=3)),
                ('state', models.CharField(choices=[('BRO', 'Bronx'), ('BRK', 'Brooklyn'), ('QNS', 'Queens'), ('MAN', 'Manhattan'), ('STN', 'Staten Island')], max_length=3)),
                ('age', models.IntegerField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='person',
            name='username',
        ),
        migrations.DeleteModel(
            name='person',
        ),
    ]
