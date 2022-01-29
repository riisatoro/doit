from dataclasses import field
from django.db.models.base import Model
from rest_framework.serializers import ModelSerializer, CharField

from app_utils.models import (
    CustomUser,
)
from app_utils.models import Order, MediaStorage


class MediaStorageSerializer(ModelSerializer):
    class Meta:
        model = MediaStorage
        fields = ['url', 'title',]


class UserDetailsSerializer(ModelSerializer):
    avatar = MediaStorageSerializer()

    class Meta:
        model = CustomUser
        fields = ['username', 'url', 'avatar',]


class OrderSerializer(ModelSerializer):
    class Meta:
        model = Order
        fields = ['title', 'rating', 'url']
