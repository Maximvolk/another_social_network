from django.shortcuts import render
from .models import Article, Comment
from django.contrib.auth.decorators import login_required


def home(request):
    queryset = Article.objects.all()
    articles = [queryset[i:i + 3] for i in range(0, len(queryset), 3)]
    context = {
        'articles': articles
    }
    return render(request, 'blog/home.html', context)


def home_category(request, category):
    queryset = Article.objects.filter(category=category)
    articles = [queryset[i:i+3] for i in range(0, len(queryset), 3)]
    context = {
        'articles': articles
    }
    return render(request, 'blog/home.html', context)


@login_required()
def article(request, category, article_id):
    article = Article.objects.get(pk=article_id)
    context = {
        'article': article
    }
    return render(request, 'blog/article.html', context)
