from django.urls import path
from .views import user, login_view


urlpatterns = [
    path('login', login_view),
    path('<str:username>', user),
]
