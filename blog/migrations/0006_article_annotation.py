# Generated by Django 2.2.4 on 2019-08-23 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20190822_1232'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='annotation',
            field=models.CharField(default='Lorem ipsum', max_length=200),
        ),
    ]