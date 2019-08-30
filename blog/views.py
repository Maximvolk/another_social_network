from django.shortcuts import render
from .models import Article, Comment
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import WriteArticleForm


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
def article(request, category, article_id):
    article = Article.objects.get(pk=article_id)
    context = {
        'article': article
    }
    return render(request, 'blog/article.html', context)


class WriteArticleView(LoginRequiredMixin, CreateView):
    template_name = 'blog/write_article.html'
    model = Article
    form_class = WriteArticleForm
    # fields = ['title', 'annotation', 'logo', 'category', 'body']

    def get_success_url(self):
        return '/home/{category}/{article_id}'.format(
            category=self.request.POST.get('category'), article_id=self.request.POST.get('id'))
