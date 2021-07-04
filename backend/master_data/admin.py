from django.contrib import admin
from db_models.models import UserType

# Register your models here.
class UserTypeAdmin(admin.ModelAdmin):
    ...

admin.site.register(UserType, UserTypeAdmin)
