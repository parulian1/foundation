# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import news.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('gallery', '0003_gallery_image_info'),
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255)),
                ('location', models.CharField(help_text=b'Youtube video url', max_length=255)),
                ('slug', models.CharField(help_text=b'Category', max_length=255)),
                ('additional_info', models.TextField(help_text=b'Additional info related to the video')),
                ('show', models.BooleanField(default=False)),
                ('created', news.fields.DateTimeField(auto_now_add=True)),
                ('modified', news.fields.DateTimeField(auto_now=True)),
                ('created_by', models.ForeignKey(related_name='video_created', editable=False, to=settings.AUTH_USER_MODEL)),
                ('modified_by', models.ForeignKey(related_name='video_modified', editable=False, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['title', 'created'],
            },
        ),
    ]
