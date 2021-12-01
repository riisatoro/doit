from django.shortcuts import render
from rest_framework.generics import ListAPIView

from app_utils.models import UserType
from app_utils.serializers import UserTypeSerializer


class UserTypeView(ListAPIView):
    queryset = UserType.objects.all()
    serializer_class = UserTypeSerializer
