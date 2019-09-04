from django.urls import path
import blog.views as views

urlpatterns = [
    path('write_article', views.WriteArticleView.as_view()),
    path('<str:category>', views.home_category),
    path('<str:category>/<pk>/', views.article),
    path('<str:category>/<pk>/update', views.UpdateArticleView.as_view()),
    path('<str:category>/<pk>/delete', views.DeleteArticleView.as_view()),
    path('<str:category>/<pk>/leave_comment', views.LeaveCommentView.as_view()),
    path('', views.home)
]
