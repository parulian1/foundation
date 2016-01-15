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

from embed_video.fields import EmbedVideoField

log = settings.LOGGER

def get_upload_to(instance, filename):
	"""
	Returns the upload location path for this instance.

	GALLERY_PATH in settings is relative to MEDIA_ROOT.
	"""
	try:
		gallery_path = settings.GALLERY_PATH
	except AttributeError:
		log.warn("""
			GALLERY_PATH not defined in settings,
			using default 'gallery_file/'""")
		gallery_path = 'gallery_file/'
	retval = "%s%s" % (gallery_path, filename)
	return retval

class Gallery(models.Model):
	title = models.CharField(max_length=255)
	image = models.ImageField(upload_to=get_upload_to, null=True, max_length=300)
	
	slug = models.CharField(max_length=255, help_text="Category")
	##adding new field for index image slider option Jan, 08-2016
	image_info = models.TextField(null=True, blank=True, help_text="this field related to show_to_index, would be label at index page")
	show_to_index = models.BooleanField(default=False, help_text="Option to show image into index page")
	#Adding new field to be option for image to be displayed or not, this will
	#help user/data admin(not administrator) not to delete the image
	show = models.BooleanField(default=True, help_text="Option to show or hide the image")
	created = DateTimeField(auto_now_add=True, editable=False)
	created_by = models.ForeignKey(User,
	                               related_name='gallery_created', editable=False)
	modified = DateTimeField(auto_now=True, editable=False)
	modified_by = models.ForeignKey(User,
	                                related_name='gallery_modified', editable=False)

	class Meta:
	    ordering = ['title', 'created']
	    

	def __unicode__(self):
	    return '%s' % (self.title)


	def save(self, *args, **kwargs):
	# Need to save first before we have access to the physical file?
		try:
		    os.stat(self.image.path)
		except OSError:
		    super(Gallery, self).save(*args, **kwargs)

		super(Gallery, self).save(*args, **kwargs)


class Video(models.Model):
	title = models.CharField(max_length=255)
	location = EmbedVideoField() # same like models.URLField()
	slug = models.CharField(max_length=255, help_text="Category")
	additional_info = models.TextField(null=True, 
						blank=True, 
						help_text="Additional info related to the video")
	show = models.BooleanField(default=False)
	created = DateTimeField(auto_now_add=True, editable=False)
	created_by = models.ForeignKey(User, related_name='video_created', editable=False)
	modified = DateTimeField(auto_now=True, editable=False)
	modified_by = models.ForeignKey(User, related_name='video_modified', editable=False)

	class Meta:
		ordering = ['title', 'created']

	def __unicode__(self):
		return '%s' %(self.title)