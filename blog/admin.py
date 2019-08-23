from django.contrib import admin
from .models import Article, Comment


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'annotation', 'logo', 'logo_preview',
                    'category', 'author', 'date_created', 'date_modified']
    exclude = ['author', 'logo_preview']

    def save_model(self, request, instance, form, change):
        if not instance.pk:
            instance.author = request.user
        super().save_model(request, instance, form, change)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['author', 'date_created', 'body', 'article']
    exclude = ['author']

    def save_model(self, request, instance, form, change):
        if not instance.pk:
            instance.author = request.user
        super().save_model(request, instance, form, change)
