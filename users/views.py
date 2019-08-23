from django.shortcuts import render
from .models import CustomUser


def user(request, username):
    user_ = CustomUser.objects.get(username=username)
    context = {
        'user': user_
    }
    return render(request, 'users/me.html', context)
