# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='gallery',
            name='show',
            field=models.BooleanField(default=True, help_text=b'Option to show or hide the image'),
        ),
        migrations.AddField(
            model_name='gallery',
            name='show_to_index',
            field=models.BooleanField(default=False, help_text=b'Option to show image into index page'),
        ),
    ]
