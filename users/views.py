from django.shortcuts import render, redirect
from .models import CustomUser
from django.contrib.auth import authenticate, login, logout


def login_view(request):
    username = request.POST['username']
    password = request.POST['password']
    user_ = authenticate(request, username=username, password=password)

    if user_ is not None:
        login(request, user_)
        if not request.POST['next']:
            return redirect('/home')
        else:
            return redirect(request.POST['next'])
    else:
        pass


def logout_view(request):
    logout(request)
    return redirect('/home')


def user(request, username):
    user_ = CustomUser.objects.get(username=username)
    context = {
        'user': user_
    }
    return render(request, 'users/me.html', context)
