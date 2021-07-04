from django.db.models import fields
from rest_framework.serializers import ModelSerializer
from db_models.models import UserType

class UserTypeSerializer(ModelSerializer):
    class Meta:
        model = UserType
        fields = ['id', 'name']