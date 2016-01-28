from django.conf.urls import url

from . import views

app_name = 'career'
urlpatterns = [
	url(r'^$', views.list, name='career_main'),
]