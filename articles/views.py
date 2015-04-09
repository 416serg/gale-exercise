from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic


from .models import Article


class IndexView(generic.ListView):
    template_name = 'articles/index.html'
    context_object_name = 'article_list'

    def get_queryset(self):
        """Return all articles"""
        return Article.objects.all()


def article(request, article_id):
    return HttpResponse("You're looking at article %s." % article_id)
