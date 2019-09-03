from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_delete
from django.dispatch import receiver
from PIL import Image, ImageOps
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile
import sys
from django.conf import settings
import os


def get_avatar_path(instance, filename):
    path = 'avatars/{username}.png'.format(username=instance.username)
    if os.path.exists(os.path.join(settings.MEDIA_ROOT, path)):
        os.remove(os.path.join(settings.MEDIA_ROOT, path))
    return path


def get_avatar_preview_path(instance, filename):
    path = 'avatars_preview/{username}.png'.format(username=instance.username)
    if os.path.exists(os.path.join(settings.MEDIA_ROOT, path)):
        os.remove(os.path.join(settings.MEDIA_ROOT, path))
    return path


class CustomUser(AbstractUser):
    description = models.CharField(max_length=256)
    avatar = models.ImageField(upload_to=get_avatar_path, default='avatars/default.png', blank=True)
    avatar_preview = models.ImageField(upload_to=get_avatar_preview_path, null=True)

    def __str__(self):
        return self.username

    def save(self, *args, **kwargs):
        # Opening uploaded image
        img = Image.open(self.avatar)

        output = BytesIO()
        output_preview = BytesIO()

        # Resize image
        img = img.resize((225, 225))
        preview = ImageOps.crop(img, (82, 82, 83, 83))

        # Save to the output
        img.save(output, format='PNG', quality=100)
        preview.save(output_preview, format='PNG', quality=100)
        output.seek(0)
        output_preview.seek(0)

        self.avatar = InMemoryUploadedFile(
            output, 'ImageField', '%s.png' % self.avatar.name.split('.')[0], 'image/png', sys.getsizeof(output), None
        )
        self.avatar_preview = InMemoryUploadedFile(
            output_preview, 'ImageField', 'avatars_preview/{username}.png'.format(username=self.username),
            'image/png', sys.getsizeof(output_preview), None
        )
        super(CustomUser, self).save(*args, **kwargs)


@receiver(post_delete, sender=CustomUser)
def delete_avatar_when_user_deleted(sender, instance, **kwargs):
    instance.avatar.delete(False)
    instance.avatar_preview.delete(False)
