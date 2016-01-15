from django import forms
from django.contrib import admin
from news.widget import AdminImageWidget, MarkItUpWidget
from .models import Gallery, Video

class GalleryAdminForm(forms.ModelForm):
	class Meta:
		model = Gallery
		fields = ['title', 'image', 'image_info', 'show_to_index', 'show', 'slug']

	def __init__(self, *args, **kwargs):
		super(GalleryAdminForm, self).__init__(*args, **kwargs)
		self.fields['image'].widget = AdminImageWidget()
		self.fields['image_info'].widget = MarkItUpWidget(attrs={'max_length': '100'})

	def clean(self):
		cleaned_data = self.cleaned_data
		return cleaned_data

class GalleryBase(object):
	list_display = ['title', 'show_to_index', 'show',  'slug', 'modified_by', 'modified']
	search_fields = ['title']
	list_filter = ['title', 'show_to_index', 'show','modified_by']

class GalleryAdmin(GalleryBase, admin.ModelAdmin):
	form = GalleryAdminForm
	def save_model(self, request, obj, form, change):
		obj.created_by = request.user
		obj.modified_by = request.user
		obj.save()

class VideoBase(object):
	list_display = ['title', 'location', 'show',  'slug', 'modified_by', 'modified']

class VideoAdmin(VideoBase, admin.ModelAdmin):
	def save_model(self, request, obj, form, change):
		obj.created_by = request.user
		obj.modified_by = request.user
		obj.save()


admin.site.register(Gallery, GalleryAdmin)
admin.site.register(Video, VideoAdmin)