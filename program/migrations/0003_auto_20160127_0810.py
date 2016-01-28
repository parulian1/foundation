# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('program', '0002_auto_20160120_0935'),
    ]

    operations = [
        migrations.AlterField(
            model_name='program',
            name='slug',
            field=models.SlugField(max_length=255),
        ),
    ]
