from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import CustomUser

from .forms import CustomUserCreationForm, CustomUserChangeForm


class UserAdmin(BaseUserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ('first_name', 'last_name', 'username', 'email', 'description', 'avatar', 'password')
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('avatar', 'first_name', 'last_name', 'email', 'description')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')})
    )

    add_fieldsets = (
        ('Login credentials', {'fields': ('username', 'password1', 'password2')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'description', 'avatar', 'email')}),
    )


admin.site.register(CustomUser, UserAdmin)
