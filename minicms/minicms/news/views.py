# coding: utf-8
from django.shortcuts import render
from news.models import Column, Article
# Create your views here.


def index(request):
    columns = Column.objects.all()
    return render(request,'news/index.html',{'columns': columns})

def column_detail(request, column_slug):
    column = Column.objects.filter(slug=column_slug)
    return render(request,'news/column_detail.html',{'column': column})

def article_detail(request, article_slug):
    article = Article.objects.filter(slug=article_slug)
    return render(request,'news/article_detail.html', {'article': article})
