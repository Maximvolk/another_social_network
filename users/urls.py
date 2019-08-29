from django.urls import path
from .views import user, login_view, user_settings


urlpatterns = [
    path('login', login_view),
    path('<str:username>', user),
    path('<str:username>/settings', user_settings),
]
