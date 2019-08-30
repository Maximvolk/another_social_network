from django.shortcuts import render, redirect
from .models import CustomUser
from blog.models import Article
from django.contrib.auth import authenticate, login
from social_network_project import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from .forms import CustomUserChangeForm, CustomUserCreationForm
from django.views.generic.edit import UpdateView, CreateView
from django.views import View
from .forms import LoginForm
from django.http import HttpResponseForbidden


class LoginView(View):
    template_name = 'registration/login.html'

    def get(self, request):
        return render(request, 'registration/login.html', {'form': LoginForm()})

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')

        user_ = authenticate(request, username=username, password=password)

        if user_ is not None:
            login(request, user_)
            if request.GET.get('next', False):
                return redirect(request.GET.get('next'))
            else:
                return redirect(settings.LOGIN_REDIRECT_URL)
        else:
            messages.error(request, 'Invalid login or password')
            return render(request, 'registration/login.html', {'form': LoginForm()})


class SignUpView(CreateView):
    template_name = 'registration/sign_up.html'
    model = CustomUser
    form_class = CustomUserCreationForm
    success_url = '/user/login'


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


class UserSettingsView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    template_name = 'users/settings.html'
    form_class = CustomUserChangeForm
    model = CustomUser
    success_message = 'Your profile has been successfully updated!'

    def get_success_url(self):
        return '/user/{username}/settings'.format(username=self.kwargs['username'])

    def get_object(self, *args, **kwargs):
        return self.model.objects.get(username=self.kwargs['username'])

    def dispatch(self, request, *args, **kwargs):
        if request.user.username != self.kwargs['username']:
            return HttpResponseForbidden()
        return super().dispatch(request, *args, **kwargs)
