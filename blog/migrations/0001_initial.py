# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-09-07 14:32
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30, verbose_name='文章标题')),
                ('describe', models.CharField(max_length=240, verbose_name='文章摘要')),
                ('content', models.TextField(verbose_name='文章内容')),
                ('author', models.CharField(max_length=20, verbose_name='作者')),
                ('release_date', models.DateField(verbose_name='发布时间')),
                ('modify_date', models.DateField(verbose_name='修改时间')),
                ('view', models.IntegerField(default=0, verbose_name='阅读量')),
                ('is_delete', models.BooleanField(default=False, verbose_name='是否被删除')),
            ],
            options={
                'verbose_name': '文章',
                'verbose_name_plural': '文章',
                'ordering': ['-release_date'],
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='分类名称')),
            ],
            options={
                'verbose_name': '文章分类',
                'verbose_name_plural': '文章分类',
            },
        ),
        migrations.CreateModel(
            name='FriendLink',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='网站名称')),
                ('description', models.CharField(blank=True, max_length=100, null=True, verbose_name='网站描述')),
                ('link', models.CharField(max_length=255, verbose_name='友情链接')),
                ('logo_link', models.CharField(max_length=255, verbose_name='logo 链接')),
                ('create_date', models.DateField(verbose_name='添加时间')),
                ('is_active', models.BooleanField(default=True, verbose_name='是否有效')),
            ],
            options={
                'verbose_name': '友情链接',
                'verbose_name_plural': '友情链接',
                'ordering': ['-create_date'],
            },
        ),
        migrations.CreateModel(
            name='KeyWord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('keyword', models.CharField(max_length=20, verbose_name='文章关键词')),
            ],
            options={
                'verbose_name': '关键词',
                'verbose_name_plural': '关键词',
            },
        ),
        migrations.CreateModel(
            name='Tags',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='标签名')),
            ],
            options={
                'verbose_name': '标签',
                'verbose_name_plural': '标签',
            },
        ),
        migrations.AddField(
            model_name='article',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Category', verbose_name='文章分类'),
        ),
        migrations.AddField(
            model_name='article',
            name='keywords',
            field=models.ManyToManyField(help_text='文章关键词,SEO 优化', to='blog.KeyWord', verbose_name='文章关键词'),
        ),
        migrations.AddField(
            model_name='article',
            name='tags',
            field=models.ManyToManyField(to='blog.Tags', verbose_name='文章标签'),
        ),
    ]
