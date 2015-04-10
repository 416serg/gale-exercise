from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from django.utils import timezone


from .models import Article


class IndexView(generic.ListView):
    template_name = 'articles/index.html'
    context_object_name = 'article_list'
    random_article = Article.objects.order_by('?')[0]

    def get_queryset(self):
        """Return all articles"""
        return Article.objects.order_by('-pub_date').filter(pub_date__lte=timezone.now())

class ArticleView(generic.DetailView):
    model = Article
    template_name = 'articles/article.html'


# def article(request, article_id):
#     try:
#         article = Articles.objects.get(pk=question_id)
#     except Question.DoesNotExist:
#         raise Http404("Article does not exist")
#     return render(request, 'articles/article.html', {'article': article})
