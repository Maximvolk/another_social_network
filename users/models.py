from django.db import models
from django.contrib.auth.models import AbstractUser
from PIL import Image
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile
import sys


def get_avatar_path(instance, filename):
    return 'avatars/{username}.{ext}'.format(username=instance.username, ext=filename.split('.')[1])


class CustomUser(AbstractUser):
    description = models.CharField(max_length=256)
    avatar = models.ImageField(upload_to=get_avatar_path, default='avatars/default.png')

    def __str__(self):
        return self.username

    def save(self, *args, **kwargs):
        # Opening uploaded image
        img = Image.open(self.avatar)

        output = BytesIO()

        # Resize image
        img = img.resize((225, 225))

        # Save to the output
        img.save(output, format='PNG', quality=100)
        output.seek(0)

        self.avatar = InMemoryUploadedFile(
            output, 'ImageField', '%s.png' % self.avatar.name.split('.')[0], 'image/png', sys.getsizeof(output), None
        )
        super(CustomUser, self).save(*args, **kwargs)
