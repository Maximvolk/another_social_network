from .forms import LoginForm


def add_login_form(request):
    return {
        'login_form': LoginForm(),
    }
