from django.shortcuts import render
from .models import Article, Comment
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import WriteArticleForm
from django.http import HttpResponseForbidden


class AuthorRequiredMixin:
    def dispatch(self, request, *args, **kwargs):
        author_ = Article.objects.get(pk=self.kwargs['pk']).author
        if request.user != author_:
            return HttpResponseForbidden()
        return super(AuthorRequiredMixin, self).dispatch(request, *args, **kwargs)


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


@login_required
def article(request, category, pk):
    article = Article.objects.get(pk=pk)
    context = {
        'article': article
    }
    return render(request, 'blog/article.html', context)


class DeleteArticleView(LoginRequiredMixin, AuthorRequiredMixin, DeleteView):
    model = Article
    success_url = '/home'
