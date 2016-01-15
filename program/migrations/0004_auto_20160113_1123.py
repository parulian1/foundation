# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import news.fields


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0004_auto_20160113_1123'),
        ('program', '0003_auto_20160111_1214'),
    ]

    operations = [
        migrations.AddField(
            model_name='program',
            name='program_category',
            field=models.ForeignKey(blank=True, to='news.Category', null=True),
        ),
        migrations.AlterField(
            model_name='program',
            name='created',
            field=news.fields.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='program',
            name='hide',
            field=models.BooleanField(default=False, verbose_name=b'Draft'),
        ),
        migrations.AlterField(
            model_name='program',
            name='modified',
            field=news.fields.DateTimeField(auto_now=True),
        ),
    ]
