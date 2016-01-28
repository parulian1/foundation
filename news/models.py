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
from django.template.defaultfilters import capfirst

from gallery.models import Gallery
from maps.models import City
from news.fields import DateTimeField
# from tinymce.models import HTMLField


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
    location = models.ForeignKey(City, 
                                blank=True,
                                null=True)
    gallery = models.ForeignKey(Gallery, 
                                blank=True, 
                                null=True,
                                related_name='news_gallery')
    content = models.TextField()
    news_category = models.ForeignKey(Category, 
                                      blank=True, 
                                      null=True)
    # content = HTMLField()
    slug = models.CharField(max_length=255)
    hide = models.BooleanField(default=False, 
                               verbose_name="Draft")
    
    created = DateTimeField(auto_now_add=True, 
                            editable=False)
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


class Blog(models.Model):
    title = models.CharField(max_length=255)
    gallery = models.ForeignKey(Gallery, blank=True, null=True,
                                   related_name='blog_gallery')
    content = models.TextField()
    category = models.ForeignKey(Category, blank=True, null=True)
    # content = HTMLField()
    slug = models.CharField(max_length=255)
    hide = models.BooleanField(default=False, verbose_name="Draft")
    
    created = DateTimeField(auto_now_add=True, editable=False)
    created_by = models.ForeignKey(User,
                                   related_name='blog_created',
                                   editable=False)
    modified = DateTimeField(auto_now=True, editable=False)
    modified_by = models.ForeignKey(User,
                                    related_name='blog_modified',
                                    editable=False)

    class Meta:
        ordering = ['title', 'created']
        

    def __unicode__(self):
        return '%s: %s' % (self.id, self.title)

    def save(self, *args, **kwargs):
        # TODO: Bypass the protection in SynchronizableModel if changing status
        # and owner?
        return super(Blog, self).save(*args, **kwargs)


class Press(models.Model):
    title = models.CharField(max_length=255)
    location = models.ForeignKey(City, blank=True, null=True)
    gallery = models.ForeignKey(Gallery, blank=True, null=True,
                                   related_name='press_gallery')
    content = models.TextField()
    category = models.ForeignKey(Category, blank=True, null=True)
    # content = HTMLField()
    slug = models.CharField(max_length=255)
    hide = models.BooleanField(default=False, verbose_name="Draft")
    
    created = DateTimeField(auto_now_add=True, editable=False)
    created_by = models.ForeignKey(User,
                                   related_name='press_created',
                                   editable=False)
    modified = DateTimeField(auto_now=True, editable=False)
    modified_by = models.ForeignKey(User,
                                    related_name='press_modified',
                                    editable=False)

    class Meta:
        ordering = ['title', 'created']
        

    def __unicode__(self):
        return '%s: %s' % (self.id, self.title)

    def location_with_content(self):
        if self.location:
            return '<strong>%s</strong> - %s' %(capfirst(self.location.name), self.content)
        else:
            return self.content

    def save(self, *args, **kwargs):
        # TODO: Bypass the protection in SynchronizableModel if changing status
        # and owner?
        return super(Press, self).save(*args, **kwargs)