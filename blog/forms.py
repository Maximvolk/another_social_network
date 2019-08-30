from django import forms
from tinymce import TinyMCE
from .models import Article


class WriteArticleForm(forms.ModelForm):
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

    title = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Title'}), max_length=256)
    annotation = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Annotation'}), max_length=150)
    logo = forms.ImageField(required=False, widget=forms.FileInput(attrs={'class': 'form-control'}))
    category = forms.ChoiceField(choices=categories, widget=forms.Select(attrs={'class': 'form-control'}))
    body = forms.CharField(widget=TinyMCE(attrs={'class': 'form-control'}, mce_attrs={'width': 800}))

    class Meta:
        model = Article
        fields = ['title', 'annotation', 'logo', 'category', 'body']
