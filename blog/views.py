from django.shortcuts import render
from .models import Article, Comment
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import WriteArticleForm
from django.http import HttpResponseForbidden


class AuthorRequiredMixin:
    def dispatch(self, request, **kwargs):
        author_ = Article.objects.get(pk=self.kwargs['pk']).author
        if request.user != author_:
            return HttpResponseForbidden()
        return super(AuthorRequiredMixin, self).dispatch(request, **kwargs)


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


class WriteArticleView(LoginRequiredMixin, CreateView):
    template_name = 'blog/write_article.html'
    model = Article
    form_class = WriteArticleForm
    success_url = '/home'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class UpdateArticleView(LoginRequiredMixin, AuthorRequiredMixin, UpdateView):
    template_name = 'blog/write_article.html'
    model = Article
    form_class = WriteArticleForm
    success_url = '/home'


class DeleteArticleView(LoginRequiredMixin, AuthorRequiredMixin, DeleteView):
    model = Article
    success_url = '/home'
