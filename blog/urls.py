from django.urls import path
from .views import home, home_category, article, WriteArticleView


urlpatterns = [
    path('write_article', WriteArticleView.as_view()),
    path('<str:category>', home_category),
    path('<str:category>/<int:article_id>', article),
    path('', home)
]
