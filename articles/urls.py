from django.conf.urls import patterns, include, url

from . import views

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    # ex: /article/5/
    url(r'^(?P<article_id>[0-9]+)/$', views.article, name='article'),
]
