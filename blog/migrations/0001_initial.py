# Generated by Django 2.2.4 on 2019-08-15 10:12

from django.db import migrations, models
import django.db.models.deletion
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256)),
                ('category', models.CharField(choices=[('Prog', 'Programming'), ('Robo', 'Robotics'), ('Math', 'Mathematics'), ('CS', 'Computer Science'), ('BC', 'Blockchain'), ('IoT', 'Internet Of Things'), ('ML', 'Machine Learning'), ('Hard', 'Hardware'), ('DO', 'DevOps')], max_length=4)),
                ('date_created', models.DateField(auto_now_add=True)),
                ('date_modified', models.DateField(auto_now=True)),
                ('body', tinymce.models.HTMLField(verbose_name='Content')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateField(auto_now_add=True)),
                ('body', models.TextField()),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Article')),
            ],
        ),
    ]
