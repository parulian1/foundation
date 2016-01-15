# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0005_auto_20160113_1125'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['name', 'created']},
        ),
        migrations.AlterField(
            model_name='news',
            name='content',
            field=tinymce.models.HTMLField(),
        ),
    ]
