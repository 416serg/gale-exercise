from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the articles index.")

def article(request, article_id):
    return HttpResponse("You're looking at article %s." % article_id)
