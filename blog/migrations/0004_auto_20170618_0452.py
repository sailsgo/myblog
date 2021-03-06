# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2017-06-18 04:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20170606_1435'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='accessrecord',
            options={'verbose_name': '\u8bbf\u95ee\u7528\u6237', 'verbose_name_plural': '\u8bbf\u95ee\u7528\u6237'},
        ),
        migrations.AlterModelOptions(
            name='article',
            options={'verbose_name': '\u6587\u7ae0', 'verbose_name_plural': '\u6587\u7ae0'},
        ),
        migrations.AlterModelOptions(
            name='author',
            options={'verbose_name': '\u7528\u6237', 'verbose_name_plural': '\u7528\u6237'},
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': '\u5206\u7c7b', 'verbose_name_plural': '\u5206\u7c7b'},
        ),
        migrations.AlterModelOptions(
            name='dailysentence',
            options={'verbose_name': '\u6bcf\u65e5\u4e00\u53e5', 'verbose_name_plural': '\u6bcf\u65e5\u4e00\u53e5'},
        ),
        migrations.AlterModelOptions(
            name='label',
            options={'verbose_name': '\u6807\u7b7e', 'verbose_name_plural': '\u6807\u7b7e'},
        ),
        migrations.AlterField(
            model_name='article',
            name='status',
            field=models.CharField(choices=[(b'0', b'\xe7\xa7\x81\xe5\xaf\x86'), (b'1', b'\xe5\x85\xac\xe5\xbc\x80')], default=b'0', max_length=3, verbose_name=b'\xe6\x98\xaf\xe5\x90\xa6\xe6\x98\xbe\xe7\xa4\xba'),
        ),
        migrations.AlterField(
            model_name='dailysentence',
            name='createTime',
            field=models.DateField(null=True, verbose_name=b'\xe6\x97\xb6\xe9\x97\xb4'),
        ),
        migrations.AlterField(
            model_name='dailysentence',
            name='status',
            field=models.CharField(choices=[(b'0', b'\xe5\x85\xac\xe5\xbc\x80'), (b'1', b'\xe7\xa7\x81\xe5\xaf\x86')], default=b'0', max_length=4, verbose_name=b'\xe6\x98\xaf\xe5\x90\xa6\xe7\x94\x9f\xe6\x95\x88'),
        ),
        migrations.AlterField(
            model_name='dailysentence',
            name='title',
            field=models.CharField(max_length=64, null=True, verbose_name=b'\xe6\xa0\x87\xe9\xa2\x98'),
        ),
    ]
