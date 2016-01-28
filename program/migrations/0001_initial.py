# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import news.fields
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0006_auto_20160113_1152'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Program',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255)),
                ('content', models.TextField()),
                ('slug', models.CharField(help_text=b'Category', max_length=255)),
                ('hide', models.BooleanField(default=False, verbose_name=b'Draft')),
                ('created', news.fields.DateTimeField(auto_now_add=True)),
                ('modified', news.fields.DateTimeField(auto_now=True)),
                ('created_by', models.ForeignKey(related_name='program_created', editable=False, to=settings.AUTH_USER_MODEL)),
                ('gallery', models.ForeignKey(related_name='program_gallery', blank=True, to='gallery.Gallery', null=True)),
                ('modified_by', models.ForeignKey(related_name='program_modified', editable=False, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['title', 'created'],
            },
        ),
        migrations.CreateModel(
            name='ProgramCategory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('additional_info', models.TextField()),
                ('created', news.fields.DateTimeField(auto_now_add=True)),
                ('modified', news.fields.DateTimeField(auto_now=True)),
                ('created_by', models.ForeignKey(related_name='programcategory_created', editable=False, to=settings.AUTH_USER_MODEL)),
                ('modified_by', models.ForeignKey(related_name='programcategory_modified', editable=False, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['name', 'created'],
            },
        ),
        migrations.AddField(
            model_name='program',
            name='program_category',
            field=models.ForeignKey(blank=True, to='program.ProgramCategory', null=True),
        ),
    ]
