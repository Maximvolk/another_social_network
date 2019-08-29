from django.shortcuts import render, redirect
from .models import CustomUser
from blog.models import Article
from django.contrib.auth import authenticate, login
from social_network_project import settings
from django.contrib.auth.decorators import login_required


def login_view(request):
    if request.method == 'GET':
        return render(request, 'registration/login.html', {})
    else:
        username = request.POST.get('uname', False)
        password = request.POST.get('pwd', False)

        user_ = authenticate(request, username=username, password=password)

        if user_ is not None:
            login(request, user_)
            if request.GET.get('next'):
                return redirect(request.GET.get('next'))
            else:
                return redirect(settings.LOGIN_REDIRECT_URL)


@login_required
def user(request, username):
    user_ = CustomUser.objects.get(username=username)
    articles_ = Article.objects.filter(author__username=user_.username)
    articles = [articles_[i:i + 3] for i in range(0, len(articles_), 3)]
    context = {
        'user': user_,
        'articles': articles
    }
    return render(request, 'users/user.html', context)


@login_required
def user_settings(request, username):
    user_ = CustomUser.objects.get(username=username)
    context = {
        'user': user_
    }

    if request.user.username == username:
        return render(request, 'users/settings.html', context)
    else:
        return redirect(settings.LOGIN_REDIRECT_URL)
