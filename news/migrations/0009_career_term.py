# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0008_auto_20160113_1427'),
    ]

    operations = [
        migrations.AddField(
            model_name='career',
            name='term',
            field=models.CharField(default=b'Internship', max_length=50, choices=[(b'Internship', b'Internship'), (b'Freelance', b'Freelance'), (b'Full Time', b'Full Time')]),
        ),
    ]
