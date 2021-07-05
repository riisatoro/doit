from django.contrib import admin
from db_models.models import CustomUser

# Register your models here.
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'slug', 'is_active']

admin.site.register(CustomUser, CustomUserAdmin)
