# Generated by Django 2.2.4 on 2019-08-22 11:12

import blog.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20190822_1108'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='logo_preview',
            field=models.ImageField(null=True, upload_to=blog.models.get_logo_preview_path),
        ),
    ]
