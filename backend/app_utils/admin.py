from django.contrib import admin
from app_utils.models import *


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'url', 'rating',)
