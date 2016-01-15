from django import forms
from django.contrib import admin

from gallery.models import Gallery
from news.models import News, Category, Career
from news.widget import MarkItUpWidget, AdminImageWidget

class NewsAdminForm(forms.ModelForm):
    image = forms.ImageField(widget=AdminImageWidget, required=False)
    class Meta:
        model = News
        fields = ['title', 'news_category', 'content', 'slug', 'hide']

    def __init__(self, *args, **kwargs):
        super(NewsAdminForm, self).__init__(*args, **kwargs)
        # self.fields['content'].widget = MarkItUpWidget()
        image_value = None
        if self.instance and self.instance.id:
            if self.instance.gallery:
                self.fields['image'].initial = self.instance.gallery.image

class NewsBase(object):
    list_display = ['title', 'news_category', 'slug', 'hide', 'modified_by', 'modified']
    search_fields = ['title']
    list_filter = ['hide', 'modified_by']


class NewsAdmin(NewsBase, admin.ModelAdmin):
    form = NewsAdminForm

    def get_form(self, request, *args, **kwargs):
        form = super(NewsAdmin, self).get_form(request, *args, **kwargs)
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

class CategoryBase(object):
    list_display = ['name', 'modified_by', 'modified']

class CategoryAdmin(CategoryBase, admin.ModelAdmin):

    def save_model(self, request, obj, form, change):
        obj.created_by = request.user
        obj.modified_by = request.user
    
        obj.save()

class CareerBase(object):
    list_display = ['title', 'show', 'modified_by', 'modified']

class CareerAdmin(CareerBase, admin.ModelAdmin):

    def save_model(self, request, obj, form, change):
        obj.created_by = request.user
        obj.modified_by = request.user
    
        obj.save()

admin.site.register(News, NewsAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Career, CareerAdmin)
