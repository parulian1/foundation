# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import news.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Career',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255)),
                ('term', models.CharField(default=b'Internship', max_length=50, choices=[(b'Internship', b'Internship'), (b'Freelance', b'Freelance'), (b'Full Time', b'Full Time')])),
                ('function', models.TextField(max_length=500)),
                ('requirement', models.TextField()),
                ('show', models.BooleanField(default=False)),
                ('created', news.fields.DateTimeField(auto_now_add=True)),
                ('modified', news.fields.DateTimeField(auto_now=True)),
                ('created_by', models.ForeignKey(related_name='career_created', editable=False, to=settings.AUTH_USER_MODEL)),
                ('modified_by', models.ForeignKey(related_name='career_modified', editable=False, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
