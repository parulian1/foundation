# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0005_auto_20160113_1146'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='additional_info',
            field=models.TextField(help_text=b'Additional info related to the video', null=True, blank=True),
        ),
    ]
