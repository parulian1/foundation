from django.conf.urls import url

from . import views

app_name = 'news'
urlpatterns = [
	url(r'^$', views.news, name='news_main'),
    url(r'^blog/$', views.blogs, name='blog_main'),
    url(r'^press/$', views.press, name='news_press'),
    url(r'^career/$', views.career, name='career'),
]