from django import forms
from django.contrib import admin

from career.models import Career
from news.widget import MarkItUpWidget

# Register your models here.

class CareerAdminForm(forms.ModelForm):
    class Meta:
        model = Career
        fields = ['title', 'term', 'function', 'requirement', 'show']

    def __init__(self, *args, **kwargs):
        super(CareerAdminForm, self).__init__(*args, **kwargs)
        self.fields['requirement'].widget = MarkItUpWidget()

class CareerBase(object):
    list_display = ['title', 'show', 'modified_by', 'modified']

class CareerAdmin(CareerBase, admin.ModelAdmin):
	form = CareerAdminForm
	def save_model(self, request, obj, form, change):
	    obj.created_by = request.user
	    obj.modified_by = request.user

	    obj.save()


admin.site.register(Career, CareerAdmin)

