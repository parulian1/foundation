# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0002_auto_20160108_1117'),
    ]

    operations = [
        migrations.AddField(
            model_name='gallery',
            name='image_info',
            field=models.TextField(help_text=b'this field related to show_to_index, would be label at index page', null=True, blank=True),
        ),
    ]
