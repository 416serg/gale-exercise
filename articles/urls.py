from django.conf.urls import patterns, include, url

from . import views

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    # ex: /article/5/
    url(r'^(?P<pk>[0-9]+)/$', views.ArticleView.as_view(), name='article'),
]
