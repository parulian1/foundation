from django.db import models
from django.contrib.auth.models import User

from news.fields import DateTimeField

# Create your models here.
class Country(models.Model):
    name = models.CharField(max_length=150)
    additional_info = models.TextField(blank=True, null=True)
    created = DateTimeField(auto_now_add=True, editable=False)
    created_by = models.ForeignKey(User, 
                                related_name='country_created', 
                                editable=False)
    modified = DateTimeField(auto_now=True, editable=False)
    modified_by = models.ForeignKey(User,
                                    related_name='country_modified',
                                    editable=False)

    class Meta:
        ordering = ['name', 'created']

    def __unicode__(self):
        return self.name


class State(models.Model):
    name = models.CharField(max_length=150)
    country = models.ForeignKey(Country)
    additional_info = models.TextField(blank=True, null=True)
    created = DateTimeField(auto_now_add=True, editable=False)
    created_by = models.ForeignKey(User,
                                   related_name='state_created',
                                   editable=False)
    modified = DateTimeField(auto_now=True, editable=False)
    modified_by = models.ForeignKey(User,
                                    related_name='state_modified',
                                    editable=False)

    class Meta:
    	ordering = ['country', 'name']

    def __unicode__(self):
    	return self.name


class City(models.Model):
    name = models.CharField(max_length=150)
    state = models.ForeignKey(State)
    additional_info = models.TextField(blank=True, null=True)
    created = DateTimeField(auto_now_add=True, editable=False)
    created_by = models.ForeignKey(User,
                                   related_name='city_created',
                                   editable=False)
    modified = DateTimeField(auto_now=True, editable=False)
    modified_by = models.ForeignKey(User,
                                    related_name='city_modified',
                                    editable=False)	

    class Meta:
    	ordering = ['state', 'name']

    def __unicode__(self):
    	# return '%s - %s' %(self.state, self.name) 
        return self.name

