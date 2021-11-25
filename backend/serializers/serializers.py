from django.db.models import fields
from django.db.models.base import Model
from rest_framework.serializers import ModelSerializer
from db_models.models import (
    UserType,
    CustomUser,
)

class UserTypeSerializer(ModelSerializer):
    class Meta:
        model = UserType
        fields = ['id', 'name']


class PrivateUserProfileSerializer(ModelSerializer):
    user_type = UserTypeSerializer()

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'user_type', 'slug', 'avatar', 'about']


class PublicUserProfileSerializer(ModelSerializer):
    user_type = UserTypeSerializer()

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'user_type', 'slug', 'avatar', 'about']
