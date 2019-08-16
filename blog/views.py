from django.shortcuts import render
from .models import Article, Comment


def home(request):
    return render(request, 'blog/home.html', {})
