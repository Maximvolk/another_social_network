# Generated by Django 2.2.4 on 2019-08-23 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20190823_0919'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='annotation',
            field=models.TextField(default='Lorem ipsum', max_length=150),
        ),
    ]
