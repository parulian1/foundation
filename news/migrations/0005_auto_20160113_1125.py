# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0004_auto_20160113_1123'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='additional_info',
            field=models.TextField(help_text=b'additional information related to category', max_length=1500, null=True, blank=True),
        ),
    ]
