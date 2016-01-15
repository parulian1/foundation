# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import blog.fields


class Migration(migrations.Migration):

    dependencies = [
        ('program', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='program',
            name='created',
            field=blog.fields.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='program',
            name='modified',
            field=blog.fields.DateTimeField(auto_now=True),
        ),
    ]
