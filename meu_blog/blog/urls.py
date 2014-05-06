from django.conf.urls import patterns, url

from blog import views

urlpatterns = patterns('',
	url(r'^$', views.list_of_articles, name = "list_of_articles"),
	url(r'^(?P<artigo_id>\d+)/$' , views.article, name = "artigo")
)
