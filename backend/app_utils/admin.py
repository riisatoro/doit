from django.contrib import admin
from app_utils.models import *


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'url', 'rating',)


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('title', 'rating', 'tag_list',)
    filter_horizontal = ('tags',)


@admin.register(OrderTag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('title', 'description',)


@admin.register(OrderApplicant)
class OrderApplicantAdmin(admin.ModelAdmin):
    list_display = ('applicant', 'order','is_approved', 'review_required',)
    filter_horizontal = ('media',)


@admin.register(MediaStorage)
class MediaStorageAdmin(admin.ModelAdmin):
    list_display = ('title', 'document', 'content_type',)