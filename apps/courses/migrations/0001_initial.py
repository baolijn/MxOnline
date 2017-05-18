# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-18 10:09
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('organization', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=52, verbose_name='\u8bfe\u7a0b\u540d\u5b57')),
                ('desc', models.CharField(max_length=300, verbose_name='\u8bfe\u7a0b\u63cf\u8ff0')),
                ('detail', models.TextField(verbose_name='\u8bfe\u7a0b\u8be6\u60c5')),
                ('degree', models.CharField(choices=[('cj', '\u521d\u7ea7'), ('zj', '\u4e2d\u7ea7'), ('gj', '\u9ad8\u7ea7')], max_length=2, verbose_name='\u96be\u5ea6')),
                ('learn_times', models.IntegerField(default=0, verbose_name='\u5b66\u4e60\u65f6\u957f(\u5206\u949f\u6570)')),
                ('students', models.IntegerField(default=0, verbose_name='\u5b66\u4e60\u4eba\u6570')),
                ('fav_nums', models.IntegerField(default=0, verbose_name='\u6536\u85cf\u4eba\u6570')),
                ('image', models.ImageField(upload_to='courses/%Y/%m', verbose_name='\u5c01\u9762\u56fe')),
                ('click_nums', models.IntegerField(default=0, verbose_name='\u70b9\u51fb\u6570')),
                ('is_banner', models.BooleanField(default=False, verbose_name='\u662f\u5426\u662f\u8f6e\u64ad\u56fe')),
                ('category', models.CharField(default='\u540e\u7aef', max_length=20, verbose_name='\u8bfe\u7a0b\u7c7b\u522b')),
                ('tag', models.CharField(default='', max_length=10, verbose_name='\u8bfe\u7a0b\u6807\u7b7e')),
                ('youneed_konw', models.CharField(default='', max_length=300, verbose_name='\u8bfe\u524d\u987b\u77e5')),
                ('teacher_tell', models.CharField(default='', max_length=300, verbose_name='\u8001\u5e08\u544a\u8bc9\u4f60\u80fd\u5b66\u4ec0\u4e48')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='\u6dfb\u52a0\u65f6\u95f4')),
                ('course_org', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='organization.CourseOrg', verbose_name='\u8bfe\u7a0b\u673a\u6784')),
                ('teacher', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='organization.Teacher', verbose_name='\u8bb2\u5e08')),
            ],
            options={
                'verbose_name': '\u8bfe\u7a0b',
                'verbose_name_plural': '\u8bfe\u7a0b',
            },
        ),
        migrations.CreateModel(
            name='CourseResource',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='\u8bfe\u4ef6\u540d')),
                ('download', models.FileField(upload_to='course/resource/%Y/%m', verbose_name='\u8d44\u6e90\u6587\u4ef6')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='\u6dfb\u52a0\u65f6\u95f4')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.Course', verbose_name='\u8bfe\u7a0b')),
            ],
            options={
                'verbose_name': '\u8bfe\u7a0b\u8d44\u6e90',
                'verbose_name_plural': '\u8bfe\u7a0b\u8d44\u6e90',
            },
        ),
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='\u7ae0\u8282\u540d')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='\u6dfb\u52a0\u65f6\u95f4')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.Course', verbose_name='\u8bfe\u7a0b')),
            ],
            options={
                'verbose_name': '\u7ae0\u8282',
                'verbose_name_plural': '\u7ae0\u8282',
            },
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='\u89c6\u9891\u540d')),
                ('url', models.URLField(default='www.baidu.com', verbose_name='\u8bbf\u95ee\u5730\u5740')),
                ('learn_times', models.IntegerField(default=0, verbose_name='\u89c6\u9891\u65f6\u957f(\u5206\u949f\u6570)')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='\u6dfb\u52a0\u65f6\u95f4')),
                ('lesson', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.Lesson', verbose_name='\u7ae0\u8282')),
            ],
            options={
                'verbose_name': '\u89c6\u9891',
                'verbose_name_plural': '\u89c6\u9891',
            },
        ),
    ]
