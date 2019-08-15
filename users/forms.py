from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    first_name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}), max_length=50)
    last_name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}), max_length=50)
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}), max_length=50)
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}))
    description = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Something about you'}),
        max_length=256,
        required=False
    )
    avatar = forms.ImageField(required=False)
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}), max_length=50)
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password again'}), max_length=50)

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('first_name', 'last_name', 'email', 'username', 'description', 'avatar', 'password1', 'password2')


class CustomUserChangeForm(UserChangeForm):
    first_name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}), max_length=50)
    last_name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}), max_length=50)
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}), max_length=50)
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}))
    description = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Something about you'}),
        max_length=256,
        required=False
    )
    avatar = forms.ImageField(required=False)
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}), max_length=50)
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password again'}), max_length=50)

    class Meta(UserChangeForm.Meta):
        model = CustomUser
        fields = ('first_name', 'last_name', 'email', 'username', 'description', 'avatar', 'password1', 'password2')
