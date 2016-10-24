# coding: utf-8
from django.shortcuts import render
# Create your views here.


def index(request):
    return render(request,'news/re.html')

def column_detail(request, column_slug):
    return render(request,'news/column_detail.html',{'column_slug': column_slug})

def article_detail(request, article_slug):
    return render(request,'news/article_detial.html', {'article_slug': article_slug})
