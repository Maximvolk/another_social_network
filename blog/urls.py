from django.urls import path
from .views import home, home_category, article


urlpatterns = [
    path('<str:category>', home_category),
    path('<str:category>/<int:article_id>', article),
    path('', home)
]
