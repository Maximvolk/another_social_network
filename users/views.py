from django.shortcuts import render, redirect
from .models import CustomUser
from django.contrib.auth import authenticate, login
from social_network_project import settings


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


def user(request, username):
    user_ = CustomUser.objects.get(username=username)
    context = {
        'user': user_
    }
    return render(request, 'users/me.html', context)
