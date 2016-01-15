import datetime
import os
import re
import time
import traceback

from decimal import Decimal

from django.conf import settings
from django.db import models, connection
from django.db.models import permalink, Max, Count
from django.core import serializers
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType

from news.fields import DateTimeField
from gallery.models import Gallery
from tinymce.models import HTMLField


class Category(models.Model):
    name = models.CharField(max_length=50)
    additional_info = models.TextField(max_length=1500, 
                        blank=True, null=True, 
                        help_text='additional information related to category')
    created = DateTimeField(auto_now_add=True, editable=False)
    created_by = models.ForeignKey(User,
                                   related_name='category_created',
                                   editable=False)
    modified = DateTimeField(auto_now=True, editable=False)
    modified_by = models.ForeignKey(User,
                                    related_name='category_modified',
                                    editable=False)

    class Meta:
        ordering = ['name', 'created']

    def __unicode__(self):
        return self.name


class News(models.Model):
    title = models.CharField(max_length=255)
    gallery = models.ForeignKey(Gallery, blank=True, null=True,
                                   related_name='news_gallery')
    # content = models.TextField(max_length=1500)
    news_category = models.ForeignKey(Category, blank=True, null=True)
    content = HTMLField()
    slug = models.CharField(max_length=255)
    hide = models.BooleanField(default=False, verbose_name="Draft")
    
    created = DateTimeField(auto_now_add=True, editable=False)
    created_by = models.ForeignKey(User,
                                   related_name='news_created',
                                   editable=False)
    modified = DateTimeField(auto_now=True, editable=False)
    modified_by = models.ForeignKey(User,
                                    related_name='news_modified',
                                    editable=False)

    class Meta:
        ordering = ['title', 'created']
        

    def __unicode__(self):
        return '%s: %s' % (self.id, self.title)

    def save(self, *args, **kwargs):
        # TODO: Bypass the protection in SynchronizableModel if changing status
        # and owner?
        return super(News, self).save(*args, **kwargs)


class Career(models.Model):
    CAREER_CHOICE = (
        ('Internship', 'Internship'),
        ('Freelance', 'Freelance'),
        ('Full Time', 'Full Time'),
    )
    title = models.CharField(max_length=255)
    term = models.CharField(max_length=50, choices=CAREER_CHOICE, default="Internship")
    function = models.TextField(max_length=500)
    requirement = HTMLField()
    show = models.BooleanField(default=False)
    created = DateTimeField(auto_now_add=True, editable=False)
    created_by = models.ForeignKey(User,
                                   related_name='career_created',
                                   editable=False)
    modified = DateTimeField(auto_now=True, editable=False)
    modified_by = models.ForeignKey(User,
                                    related_name='career_modified',
                                    editable=False)