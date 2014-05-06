from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from meu_blog import views

urlpatterns = patterns('',
   	url(r'^$', views.index),
    url(r'^artigo/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
)