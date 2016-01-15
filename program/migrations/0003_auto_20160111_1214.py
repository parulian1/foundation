# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('program', '0002_auto_20160108_1327'),
    ]

    operations = [
        migrations.AlterField(
            model_name='program',
            name='content',
            field=tinymce.models.HTMLField(max_length=1500),
        ),
    ]
