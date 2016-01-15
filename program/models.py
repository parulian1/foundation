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
from news.models import Category
from gallery.models import Gallery
from tinymce.models import HTMLField

class Program(models.Model):
    title = models.CharField(max_length=255)
    gallery = models.ForeignKey(Gallery, blank=True, null=True,
                                   related_name='program_gallery')
    program_category = models.ForeignKey(Category, blank=True, null=True)
    content = HTMLField()
    # content = MarkupField()
    slug = models.CharField(max_length=255, help_text="Category")
    hide = models.BooleanField(default=False, verbose_name="Draft")
    
    created = DateTimeField(auto_now_add=True, editable=False)
    created_by = models.ForeignKey(User,
                                   related_name='program_created', editable=False)
    modified = DateTimeField(auto_now=True, editable=False)
    modified_by = models.ForeignKey(User,
                                    related_name='program_modified', editable=False)

    class Meta:
        ordering = ['title', 'created']
        

    def __unicode__(self):
        return '%s' % (self.title)


    def image(self):
        if self.gallery:
            return self.gallery.image
        else: 
            return None
