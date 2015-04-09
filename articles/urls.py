from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    # ex: /article/5/
    url(r'^(?P<article_id>[0-9]+)/$', views.article, name='article'),
]
