# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2017-06-18 16:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20170618_0452'),
    ]

    operations = [
        migrations.AddField(
            model_name='accessrecord',
            name='accessCount',
            field=models.IntegerField(default=1, null=True, verbose_name=b'\xe5\xbd\x93\xe5\xa4\xa9\xe8\xae\xbf\xe9\x97\xae\xe6\xac\xa1\xe6\x95\xb0'),
        ),
    ]