# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import news.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('news', '0003_auto_20160108_1846'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('additional_info', models.TextField(help_text=b'additional information related to category', max_length=1500)),
                ('created', news.fields.DateTimeField(auto_now_add=True)),
                ('modified', news.fields.DateTimeField(auto_now=True)),
                ('created_by', models.ForeignKey(related_name='category_created', editable=False, to=settings.AUTH_USER_MODEL)),
                ('modified_by', models.ForeignKey(related_name='category_modified', editable=False, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterField(
            model_name='news',
            name='hide',
            field=models.BooleanField(default=False, verbose_name=b'Draft'),
        ),
        migrations.AlterField(
            model_name='news',
            name='slug',
            field=models.CharField(max_length=255),
        ),
        migrations.AddField(
            model_name='news',
            name='news_category',
            field=models.ForeignKey(blank=True, to='news.Category', null=True),
        ),
    ]
