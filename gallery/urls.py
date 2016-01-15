from django.conf.urls import url

from . import views

app_name = 'gallery'
urlpatterns = [
    url(r'^$', views.gallery, name='gallery'),
    url(r'^video/(?P<video_id>\d+)/$', views.view_video, name='view_video'),
]