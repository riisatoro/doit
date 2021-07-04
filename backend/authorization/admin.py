from django.contrib import admin
from db_models.models import CustomUser

# Register your models here.
class CustomUserAdmin(admin.ModelAdmin):
    ...

admin.site.register(CustomUser, CustomUserAdmin)
