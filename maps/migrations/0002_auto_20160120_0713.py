# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('maps', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='city',
            name='additional_info',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='country',
            name='additional_info',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='state',
            name='additional_info',
            field=models.TextField(null=True, blank=True),
        ),
    ]
