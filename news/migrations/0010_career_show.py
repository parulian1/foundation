# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0009_career_term'),
    ]

    operations = [
        migrations.AddField(
            model_name='career',
            name='show',
            field=models.BooleanField(default=False),
        ),
    ]
