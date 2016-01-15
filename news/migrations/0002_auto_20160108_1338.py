# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='created_by',
            field=models.ForeignKey(related_name='news_created', editable=False, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='news',
            name='gallery',
            field=models.ForeignKey(related_name='news_gallery', blank=True, to='gallery.Gallery', null=True),
        ),
        migrations.AlterField(
            model_name='news',
            name='modified_by',
            field=models.ForeignKey(related_name='news_modified', editable=False, to=settings.AUTH_USER_MODEL),
        ),
    ]
