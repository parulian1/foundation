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
            name='News',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255)),
                ('content', models.TextField(max_length=1500)),
                ('slug', models.CharField(help_text=b'Category', max_length=255)),
                ('hide', models.BooleanField(default=False)),
                ('created', news.fields.DateTimeField(auto_now_add=True)),
                ('modified', news.fields.DateTimeField(auto_now=True)),
                ('created_by', models.ForeignKey(related_name='blog_created', editable=False, to=settings.AUTH_USER_MODEL)),
                ('gallery', models.ForeignKey(related_name='blog_gallery', blank=True, to='gallery.Gallery', null=True)),
                ('modified_by', models.ForeignKey(related_name='blog_modified', editable=False, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['title', 'created'],
            },
        ),
    ]
