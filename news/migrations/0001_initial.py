# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import news.fields
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0006_auto_20160113_1152'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('maps', '0002_auto_20160120_0713'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255)),
                ('content', models.TextField()),
                ('slug', models.CharField(max_length=255)),
                ('hide', models.BooleanField(default=False, verbose_name=b'Draft')),
                ('created', news.fields.DateTimeField(auto_now_add=True)),
                ('modified', news.fields.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['title', 'created'],
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('additional_info', models.TextField(help_text=b'additional information related to category', max_length=1500, null=True, blank=True)),
                ('created', news.fields.DateTimeField(auto_now_add=True)),
                ('modified', news.fields.DateTimeField(auto_now=True)),
                ('created_by', models.ForeignKey(related_name='category_created', editable=False, to=settings.AUTH_USER_MODEL)),
                ('modified_by', models.ForeignKey(related_name='category_modified', editable=False, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['name', 'created'],
            },
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255)),
                ('content', models.TextField()),
                ('slug', models.CharField(max_length=255)),
                ('hide', models.BooleanField(default=False, verbose_name=b'Draft')),
                ('created', news.fields.DateTimeField(auto_now_add=True)),
                ('modified', news.fields.DateTimeField(auto_now=True)),
                ('created_by', models.ForeignKey(related_name='news_created', editable=False, to=settings.AUTH_USER_MODEL)),
                ('gallery', models.ForeignKey(related_name='news_gallery', blank=True, to='gallery.Gallery', null=True)),
                ('location', models.ForeignKey(blank=True, to='maps.City', null=True)),
                ('modified_by', models.ForeignKey(related_name='news_modified', editable=False, to=settings.AUTH_USER_MODEL)),
                ('news_category', models.ForeignKey(blank=True, to='news.Category', null=True)),
            ],
            options={
                'ordering': ['title', 'created'],
            },
        ),
        migrations.CreateModel(
            name='Press',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255)),
                ('content', models.TextField()),
                ('slug', models.CharField(max_length=255)),
                ('hide', models.BooleanField(default=False, verbose_name=b'Draft')),
                ('created', news.fields.DateTimeField(auto_now_add=True)),
                ('modified', news.fields.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(blank=True, to='news.Category', null=True)),
                ('created_by', models.ForeignKey(related_name='press_created', editable=False, to=settings.AUTH_USER_MODEL)),
                ('gallery', models.ForeignKey(related_name='press_gallery', blank=True, to='gallery.Gallery', null=True)),
                ('location', models.ForeignKey(blank=True, to='maps.City', null=True)),
                ('modified_by', models.ForeignKey(related_name='press_modified', editable=False, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['title', 'created'],
            },
        ),
        migrations.AddField(
            model_name='blog',
            name='category',
            field=models.ForeignKey(blank=True, to='news.Category', null=True),
        ),
        migrations.AddField(
            model_name='blog',
            name='created_by',
            field=models.ForeignKey(related_name='blog_created', editable=False, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='blog',
            name='gallery',
            field=models.ForeignKey(related_name='blog_gallery', blank=True, to='gallery.Gallery', null=True),
        ),
        migrations.AddField(
            model_name='blog',
            name='modified_by',
            field=models.ForeignKey(related_name='blog_modified', editable=False, to=settings.AUTH_USER_MODEL),
        ),
    ]
