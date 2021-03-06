"""foundation URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf import settings
from django.conf.urls import include, patterns, url
from django.conf.urls.static import static
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^career/', include('career.urls')),
    url(r'^gallery/', include('gallery.urls')),
    url(r'^impact/$', views.impact, name='impact'),
    url(r'^news/', include('news.urls')),
    url(r'^pillar/education/$', views.pillar_education, name='pillar_education'),
    url(r'^pillar/health/$', views.pillar_health, name='pillar_health'),
    url(r'^program/', include('program.urls')),
    url(r'^story/$', views.story, name='story'),
    url(r'^supportus/$', views.support_us, name='support_us'),
    url(r'^admin/', admin.site.urls),
    url(r'^something/paypal/', include('paypal.standard.ipn.urls')),
    # url(r'^tinymce/', include('tinymce.urls')),
] 


# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
