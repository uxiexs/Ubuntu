from django.shortcuts import render

# Create your views here.

def index(request):
	return render(request, 'blog/index.html')

def columns(request):
	return render(request, 'blog/columns.html')