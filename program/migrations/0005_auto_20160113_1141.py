# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('program', '0004_auto_20160113_1123'),
    ]

    operations = [
        migrations.AlterField(
            model_name='program',
            name='content',
            field=tinymce.models.HTMLField(),
        ),
    ]
