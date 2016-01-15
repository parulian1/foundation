# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import embed_video.fields


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0004_video'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='location',
            field=embed_video.fields.EmbedVideoField(),
        ),
    ]
