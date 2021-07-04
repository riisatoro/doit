from typing import List
from django.shortcuts import render
from rest_framework.generics import ListAPIView
from db_models.models import UserType
from serializers import UserTypeSerializer

class UserTypeView(ListAPIView):
    queryset = UserType.objects.all()
    serializer_class = UserTypeSerializer
