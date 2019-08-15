from django.db import models
from django.contrib.auth import get_user_model
from tinymce import HTMLField


class Article(models.Model):
    categories = [
        ('Prog', 'Programming'),
        ('Robo', 'Robotics'),
        ('Math', 'Mathematics'),
        ('CS', 'Computer Science'),
        ('BC', 'Blockchain'),
        ('IoT', 'Internet Of Things'),
        ('ML', 'Machine Learning'),
        ('Hard', 'Hardware'),
        ('DO', 'DevOps')
    ]

    title = models.CharField(max_length=256)
    category = models.CharField(max_length=4, choices=categories)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    date_created = models.DateField(auto_now_add=True)
    date_modified = models.DateField(auto_now=True)
    body = HTMLField('Content')

    def __str__(self):
        return self.title


class Comment(models.Model):
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    date_created = models.DateField(auto_now_add=True)
    body = models.TextField()
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
