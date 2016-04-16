# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-04-15 19:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scholarship', '0008_auto_20160415_1838'),
    ]

    operations = [
        migrations.AlterField(
            model_name='options',
            name='option_state',
            field=models.CharField(choices=[('MH', 'Maharastra'), ('UK', 'Uttarakhand'), ('UP', 'Uttar Pradesh'), ('DL', 'Delhi'), ('WB', 'West Bangal')], default='MH', max_length=3),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='state',
            field=models.CharField(choices=[('MH', 'Maharastra'), ('UK', 'Uttarakhand'), ('UP', 'Uttar Pradesh'), ('DL', 'Delhi'), ('WB', 'West Bangal')], default='MH', max_length=3),
        ),
    ]
