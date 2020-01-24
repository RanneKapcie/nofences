from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from .models import CustomUserModel

class CustomUserAdmin(UserAdmin):
    model = CustomUserModel
    list_display = ['email', 'username',]

admin.site.register(CustomUserModel, CustomUserAdmin)
