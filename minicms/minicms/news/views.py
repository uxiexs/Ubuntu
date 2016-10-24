# coding: utf-8
from django.shortcuts import render

# Create your views here.


def first_page(request):
    return render(request,'news/re.html')
