from django.conf.urls import url

from . import views

app_name = 'news'
urlpatterns = [
	url(r'^$', views.news, name='news_main'),
    url(r'^blog/$', views.blogs, name='blog_main'),
    url(r'^press/$', views.press, name='news_press'),
    url(r'^press/category/(?P<category_id>\d+)/$', views.view_press_by_category, name='view_press_by_category'),
    url(r'^press/detail/(?P<press_id>\d+)/$', views.view_press, name='view_press'),
]