from django.db import models
from django.contrib.auth import get_user_model
from tinymce import HTMLField
from io import BytesIO
from PIL import Image
from django.core.files.uploadedfile import InMemoryUploadedFile
import sys
import os
from datetime import datetime
from django.db.models.signals import post_delete
from django.dispatch import receiver
from django.conf import settings


def get_logo_path(instance, filename):
    timestamp = int(datetime.now().timestamp())
    path = 'articles/logo/{timestamp}.png'.format(timestamp=timestamp)
    if os.path.exists(os.path.join(settings.MEDIA_ROOT, path)):
        os.remove(os.path.join(settings.MEDIA_ROOT, path))
    return path


def get_logo_preview_path(instance, filename):
    timestamp = int(datetime.now().timestamp())
    path = 'articles/logo_preview/{timestamp}.png'.format(timestamp=timestamp)
    if os.path.exists(os.path.join(settings.MEDIA_ROOT, path)):
        os.remove(os.path.join(settings.MEDIA_ROOT, path))
    return path


class Article(models.Model):
    categories = [
        ('prog', 'Programming'),
        ('robo', 'Robotics'),
        ('math', 'Mathematics'),
        ('cs', 'Computer Science'),
        ('bc', 'Blockchain'),
        ('iot', 'Internet Of Things'),
        ('ml', 'Machine Learning'),
        ('hard', 'Hardware'),
        ('do', 'DevOps')
    ]

    title = models.CharField(max_length=256)
    annotation = models.TextField(max_length=150, default='Lorem ipsum')
    logo = models.ImageField(upload_to=get_logo_path, null=True)
    logo_preview = models.ImageField(upload_to=get_logo_preview_path, null=True)
    category = models.CharField(max_length=4, choices=categories)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    date_created = models.DateField(auto_now_add=True)
    date_modified = models.DateField(auto_now=True)
    body = HTMLField('Content')

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        # Resize logo_preview of article
        # Open image
        img = Image.open(self.logo)
        output = BytesIO()

        # Resize image
        img = img.resize((300, 185))

        # Save to the output
        img.save(output, format='PNG', quality=100)
        output.seek(0)

        self.logo_preview = InMemoryUploadedFile(
            output, 'ImageField', '%s.png' % get_logo_preview_path(self, ''), 'image/png', sys.getsizeof(output), None
        )
        super(Article, self).save(*args, **kwargs)


class Comment(models.Model):
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    date_created = models.DateField(auto_now_add=True)
    body = models.TextField()
    article = models.ForeignKey(Article, on_delete=models.CASCADE)


@receiver(post_delete, sender=Article)
def delete_logo_when_article_deleted(sender, instance, **kwargs):
    instance.logo.delete(False)
    instance.logo_preview.delete(False)
