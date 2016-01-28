from django import forms
from django.contrib import admin

from maps.models import Country, State, City
from news.widget import MarkItUpWidget

class CountryAdminForm(forms.ModelForm):
    class Meta:
        model = Country
        fields = ['name', 'additional_info']

    def __init__(self, *args, **kwargs):
        super(CountryAdminForm, self).__init__(*args, **kwargs)
        self.fields['additional_info'].widget = MarkItUpWidget()


class CountryBase(object):
    list_display = ['name', 'modified_by', 'modified']
    search_fields = ['name']


class CountryAdmin(CountryBase, admin.ModelAdmin):
    form = CountryAdminForm

    def get_form(self, request, *args, **kwargs):
        form = super(CountryAdmin, self).get_form(request, *args, **kwargs)
        form.request = request
        return form
    def save_model(self, request, obj, form, change):
        obj.created_by = request.user
        obj.modified_by = request.user
        obj.save()


class StateAdminForm(forms.ModelForm):
    class Meta:
        model = State
        fields = ['name', 'country', 'additional_info']

    def __init__(self, *args, **kwargs):
        super(StateAdminForm, self).__init__(*args, **kwargs)
        self.fields['additional_info'].widget = MarkItUpWidget()

class StateBase(object):
    list_display = ['name', 'country', 'modified_by', 'modified']
    search_fields = ['name', 'country']
    list_filter = ['country']


class StateAdmin(StateBase, admin.ModelAdmin):
    form = StateAdminForm

    def get_form(self, request, *args, **kwargs):
        form = super(StateAdmin, self).get_form(request, *args, **kwargs)
        form.request = request
        return form
    def save_model(self, request, obj, form, change):
        obj.created_by = request.user
        obj.modified_by = request.user
        obj.save()


class CityAdminForm(forms.ModelForm):
    class Meta:
        model = City
        fields = ['name', 'state', 'additional_info']

    def __init__(self, *args, **kwargs):
        super(CityAdminForm, self).__init__(*args, **kwargs)
        self.fields['additional_info'].widget = MarkItUpWidget()

class CityBase(object):
    list_display = ['name', 'state', 'modified_by', 'modified']
    search_fields = ['name', 'state']
    list_filter = ['state']


class CityAdmin(CityBase, admin.ModelAdmin):
    form = CityAdminForm

    def get_form(self, request, *args, **kwargs):
        form = super(CityAdmin, self).get_form(request, *args, **kwargs)
        form.request = request
        return form
    def save_model(self, request, obj, form, change):
        obj.created_by = request.user
        obj.modified_by = request.user
        obj.save()


admin.site.register(Country, CountryAdmin)
admin.site.register(State, StateAdmin)
admin.site.register(City, CityAdmin)