from django import forms
from django.contrib import admin
from program.models import Program
from news.widget import MarkItUpWidget, AdminImageWidget
from gallery.models import Gallery

from django.shortcuts import render_to_response, get_object_or_404


class ProgramAdminForm(forms.ModelForm):
    image = forms.ImageField(widget=AdminImageWidget, required=False)
    class Meta:
        model = Program
        fields = ['title', 'program_category','content', 'slug', 'hide']

    def __init__(self, *args, **kwargs):
        super(ProgramAdminForm, self).__init__(*args, **kwargs)
        # self.fields['content'].widget = MarkItUpWidget()
        image_value = None
        if self.instance and self.instance.id:
            if self.instance.gallery:
                self.fields['image'].initial = self.instance.gallery.image

    def clean(self):
        cleaned_data = self.cleaned_data
        return cleaned_data


class ProgramBase(object):
    list_display = ['title', 'program_category', 'slug', 'hide', 'modified_by', 'modified']
    search_fields = ['title']
    list_filter = ['hide', 'modified_by']


class ProgramAdmin(ProgramBase, admin.ModelAdmin):
    form = ProgramAdminForm

    def get_form(self, request, *args, **kwargs):
        form = super(ProgramAdmin, self).get_form(request, *args, **kwargs)
        form.request = request
        # if self['id']:
        #     gallery = get_object_or_404(Gallery, id=self.id)
        #     form.image = gallery.image
        return form
    def save_model(self, request, obj, form, change):
        obj.created_by = request.user
        obj.modified_by = request.user
        if form.cleaned_data.get('image'):
            if obj.gallery:
                gallery_fk = obj.gallery
                gallery_fk.title=obj.title
            else:
                # gallery_fk = Gallery.objects.create()
                gallery_fk = Gallery(title=obj.title)
            
            gallery_fk.image=form.cleaned_data.get('image') 
            gallery_fk.created_by=request.user
            gallery_fk.modified_by=request.user
            gallery_fk.save()
            obj.gallery = gallery_fk
        obj.save()

admin.site.register(Program, ProgramAdmin)