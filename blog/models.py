from django.db import models
from django.conf import settings


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
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    date_created = models.DateField(auto_now_add=True)
    date_modified = models.DateField(auto_now=True)

    # TODO: Add body field (decide how to store it)
