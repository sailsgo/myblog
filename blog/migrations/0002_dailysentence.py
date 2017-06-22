# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DailySentence',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name=b'\xe6\xaf\x8f\xe6\x97\xa5\xe4\xb8\x80\xe5\x8f\xa5', primary_key=True)),
                ('title', models.CharField(max_length=b'64', null=True, verbose_name=b'\xe6\xa0\x87\xe9\xa2\x98')),
                ('dailycontent', models.TextField(null=True, verbose_name=b'\xe5\x86\x85\xe5\xae\xb9')),
                ('status', models.CharField(default=b'0', max_length=b'4', verbose_name=b'\xe6\x98\xaf\xe5\x90\xa6\xe7\x94\x9f\xe6\x95\x88', choices=[(b'0', b'\xe4\xb8\x8d\xe7\x94\x9f\xe6\x95\x88'), (b'1', b'\xe7\x94\x9f\xe6\x95\x88')])),
                ('createTime', models.DateTimeField(null=True, verbose_name=b'\xe6\x97\xb6\xe9\x97\xb4')),
            ],
        ),
    ]
