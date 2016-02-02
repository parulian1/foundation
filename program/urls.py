from django.conf.urls import url

from . import views

app_name='program'
urlpatterns = [
    url(r'^$', views.programs, name='program_main'),
    url(r'^help/$', views.program_help, name='program_help'),
    url(r'^hope/$', views.program_hope, name='program_hope'),
    url(r'^hold/$', views.program_hold, name='program_hold'),
    url(r'^impact/$', views.impact, name='program_impact'),
    url(r'^category/(?P<category_id>\d+)/$', views.view_category, name='view_program_by_category'),
    url(r'^view/(?P<program_id>\d+)/$', views.view_program, name='view_program'),
    url(r'^donate/$', views.view_that_asks_for_money, name='program_donate'),
]