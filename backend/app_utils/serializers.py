from django.db.models.base import Model
from rest_framework.serializers import ModelSerializer, CharField

from app_utils.models import (
    UserType,
    CustomUser,
    StockOrder, 
    StockOrderTag, 
    StockOrderApplicant,
)


class UserTypeSerializer(ModelSerializer):
    class Meta:
        model = UserType
        fields = ['id', 'name']


class PrivateUserProfileSerializer(ModelSerializer):
    user_type = UserTypeSerializer()

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'user_type', 'url', 'avatar', 'about']


class PublicUserProfileSerializer(ModelSerializer):
    user_type = UserTypeSerializer()

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'user_type', 'url', 'avatar', 'about']


class ShortUserDetails(ModelSerializer):
     class Meta:
        model = CustomUser
        fields = ['name', 'url', 'avatar']


class TagSerializer(ModelSerializer):
    class Meta:
        model = StockOrderTag
        fields = ['title',]


class OrderListSerializer(ModelSerializer):
    tags = TagSerializer(read_only=True, many=True)
    author = ShortUserDetails()

    class Meta:
        model = StockOrder
        fields = ['title', 'url', 'author', 'tags', 'price']


class OrderDetailSerializer(ModelSerializer):
    tags = TagSerializer(read_only=True, many=True)
    author = ShortUserDetails()
    applicants = ShortUserDetails(read_only=True, many=True)

    class Meta:
        model = StockOrder
        fields = [
            'title', 'url', 'author', 'tags', 'description', 
            'price', 'order_status', 'executor', 'applicants',
            'due_date',
        ]


class StockOrderApplicantSerializer(ModelSerializer):
    applicant = ShortUserDetails()

    class Meta:
        model = StockOrderApplicant
        fields = ['applicant', 'message']