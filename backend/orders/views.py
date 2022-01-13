from django.shortcuts import render
from django.db.models import Q
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated

from app_utils.models import Order
from app_utils.serializers import OrderSerializer


class OrderView(ListAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class ApplyToOrderView(APIView):
    permission_classes = (IsAuthenticated,)



class SendApproveOrderView(APIView):
    permission_classes = (IsAuthenticated,)
