from django.contrib import admin
from db_models.models import *


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'user_type', 'slug', 'money',)

@admin.register(UserType)
class UserTypeAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(StockOrderApplicant)
class StockOrderApplicantAdmin(admin.ModelAdmin):
    list_display = ('applicant', 'order', 'message',)

@admin.register(StockOrderTag)
class StockOrderTagsAdmin(admin.ModelAdmin):
    fileds = ('title', 'description',)

@admin.register(StockOrder)
class StockOrder(admin.ModelAdmin):
    list_display = (
        'title', 'description', 'order_status', 'author', 'executor',
        'price', 'due_date',
    )
    readonly_fields = ('slug',)
    filter_horizontal = ('tags',)