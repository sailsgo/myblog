# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_dailysentence'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='accessrecord',
            options={'verbose_name': '\u8bbf\u95ee\u8005'},
        ),
        migrations.AlterModelOptions(
            name='article',
            options={'verbose_name': '\u6587\u7ae0'},
        ),
        migrations.AlterModelOptions(
            name='author',
            options={'verbose_name': '\u7528\u6237'},
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': '\u5206\u7c7b'},
        ),
        migrations.AlterModelOptions(
            name='dailysentence',
            options={'verbose_name': '\u6bcf\u65e5\u4e00\u53e5'},
        ),
        migrations.AlterModelOptions(
            name='label',
            options={'verbose_name': '\u6807\u7b7e'},
        ),
        migrations.AddField(
            model_name='label',
            name='labelColor',
            field=models.CharField(max_length=3, null=True, verbose_name=b'\xe8\xbe\xb9\xe6\xa1\x86\xe8\x89\xb2', choices=[(b'1', b'Green'), (b'2', b'orange'), (b'3', b'blue'), (b'4', b'red'), (b'5', b'purple'), (b'6', b'yellow')]),
        ),
    ]
