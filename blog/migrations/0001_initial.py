# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AccessRecord',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('ip', models.CharField(max_length=30, null=True, verbose_name=b'\xe8\xae\xbf\xe9\x97\xaeIP')),
                ('accessTime', models.DateTimeField(null=True, verbose_name=b'\xe6\x97\xb6\xe9\x97\xb4')),
            ],
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name=b'\xe6\x96\x87\xe7\xab\xa0ID', primary_key=True)),
                ('title', models.CharField(max_length=100, null=True, verbose_name=b'\xe6\x96\x87\xe7\xab\xa0\xe6\xa0\x87\xe9\xa2\x98')),
                ('publishDate', models.DateField(null=True, verbose_name=b'\xe5\x8f\x91\xe8\xa1\xa8\xe6\x97\xa5\xe6\x9c\x9f')),
                ('image', models.ImageField(upload_to=b'', verbose_name=b'\xe7\xae\x80\xe4\xbb\x8b\xe5\x9b\xbe')),
                ('readCount', models.IntegerField(verbose_name=b'\xe9\x98\x85\xe8\xaf\xbb\xe6\xac\xa1\xe6\x95\xb0')),
                ('content', models.TextField(verbose_name=b'\xe6\x96\x87\xe7\xab\xa0\xe5\x86\x85\xe5\xae\xb9')),
                ('intro', models.CharField(max_length=100, verbose_name=b'\xe6\x96\x87\xe7\xab\xa0\xe7\xae\x80\xe4\xbb\x8b')),
                ('status', models.CharField(default=b'0', max_length=b'3', verbose_name=b'\xe6\x98\xaf\xe5\x90\xa6\xe6\x98\xbe\xe7\xa4\xba', choices=[(b'0', b'\xe4\xb8\x8d\xe6\x98\xbe\xe7\xa4\xba'), (b'1', b'\xe5\x8f\xaf\xe6\x98\xbe\xe7\xa4\xba')])),
            ],
        ),
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name=b'\xe4\xbd\x9c\xe8\x80\x85ID', primary_key=True)),
                ('name', models.CharField(max_length=30, null=True)),
                ('password', models.CharField(max_length=30, null=True)),
                ('email', models.EmailField(max_length=30)),
                ('realName', models.CharField(max_length=30, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name=b'\xe7\xb1\xbb\xe5\x88\xabID', primary_key=True)),
                ('cateName', models.CharField(max_length=30, null=True, verbose_name=b'\xe7\xb1\xbb\xe5\x88\xab\xe5\x90\x8d\xe7\xa7\xb0')),
            ],
        ),
        migrations.CreateModel(
            name='Label',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name=b'\xe6\xa0\x87\xe7\xad\xbeID', primary_key=True)),
                ('labelName', models.CharField(max_length=30, null=True, verbose_name=b'\xe6\xa0\x87\xe7\xad\xbe\xe5\x90\x8d')),
            ],
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name=b'\xe6\x96\xb0\xe9\x97\xbbID', primary_key=True)),
                ('newsTitle', models.CharField(max_length=100, null=True, verbose_name=b'\xe6\x96\xb0\xe9\x97\xbb\xe6\xa0\x87\xe9\xa2\x98')),
                ('newsContent', models.TextField(verbose_name=b'\xe6\x96\xb0\xe9\x97\xbb\xe5\x86\x85\xe5\xae\xb9')),
                ('coverImage', models.ImageField(upload_to=b'', verbose_name=b'\xe5\xb0\x81\xe9\x9d\xa2\xe8\xbd\xae\xe6\x92\xad\xe5\x9b\xbe')),
                ('createTime', models.DateTimeField(null=True, verbose_name=b'\xe6\x96\xb0\xe9\x97\xbb\xe9\x87\x87\xe9\x9b\x86\xe6\x97\xb6\xe9\x97\xb4')),
                ('status', models.CharField(default=b'0', max_length=16, null=True, verbose_name=b'\xe6\x98\xaf\xe5\x90\xa6\xe7\x94\x9f\xe6\x95\x88', choices=[(b'0', b'\xe4\xb8\x8d\xe7\x94\x9f\xe6\x95\x88'), (b'1', b'\xe7\x94\x9f\xe6\x95\x88')])),
            ],
        ),
        migrations.AddField(
            model_name='article',
            name='author',
            field=models.ForeignKey(verbose_name=b'\xe4\xbd\x9c\xe8\x80\x85', to='blog.Author'),
        ),
        migrations.AddField(
            model_name='article',
            name='category',
            field=models.ForeignKey(verbose_name=b'\xe6\x96\x87\xe7\xab\xa0\xe7\xb1\xbb\xe5\x88\xab', to='blog.Category'),
        ),
        migrations.AddField(
            model_name='article',
            name='label',
            field=models.ManyToManyField(to='blog.Label', verbose_name=b'\xe6\x96\x87\xe7\xab\xa0\xe6\xa0\x87\xe7\xad\xbe'),
        ),
    ]
