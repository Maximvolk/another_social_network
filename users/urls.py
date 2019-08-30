from django.urls import path
from .views import user, LoginView, UserSettingsView, SignUpView


urlpatterns = [
    path('login', LoginView.as_view()),
    path('sign_up', SignUpView.as_view()),
    path('<str:username>', user),
    path('<str:username>/settings', UserSettingsView.as_view()),
]
