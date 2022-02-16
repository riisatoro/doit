from django.forms import BooleanField
from rest_framework.serializers import ModelSerializer

from app_utils.models import (
    CustomUser,
)
from app_utils.models import Order, MediaStorage, OrderApplicant


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
    review_required = BooleanField(required=False)

    class Meta:
        model = Order
        fields = ['title', 'rating', 'url', 'slug', 'description',]


class OrderApplicantSezializer(ModelSerializer):
    applicant = UserDetailsSerializer()
    order = OrderSerializer()

    class Meta:
        model = OrderApplicant
        fields = ['applicant', 'order', 'review_required', 'is_approved']
