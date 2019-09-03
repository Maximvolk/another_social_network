from django.urls import path
from .views import home, home_category, article, WriteArticleView, UpdateArticleView


urlpatterns = [
    path('write_article', WriteArticleView.as_view()),
    path('<str:category>', home_category),
    path('<str:category>/<pk>', article),
    path('<str:category>/<pk>/update', UpdateArticleView.as_view()),
    path('', home)
]
