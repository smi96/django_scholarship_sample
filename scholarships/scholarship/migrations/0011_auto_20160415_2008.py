# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-04-15 20:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scholarship', '0010_auto_20160415_2005'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='category',
            field=models.CharField(choices=[('GN', 'General'), ('OBC', 'OBC'), ('SC/ST', 'SC/ST')], default='GN', max_length=10),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='state',
            field=models.CharField(choices=[('MH', 'Maharastra'), ('UK', 'Uttarakhand'), ('UP', 'Uttar Pradesh'), ('DL', 'Delhi'), ('WB', 'West Bangal')], default='MH', max_length=10),
        ),
    ]
