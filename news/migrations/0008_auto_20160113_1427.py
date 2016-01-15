# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0007_career'),
    ]

    operations = [
        migrations.AlterField(
            model_name='career',
            name='requirement',
            field=tinymce.models.HTMLField(),
        ),
    ]
