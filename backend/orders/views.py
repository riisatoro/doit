from cgitb import lookup
from django.shortcuts import render
from django.db.models import Q
from rest_framework.views import APIView, Response
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticated

from app_utils.models import Order
from app_utils.serializers import OrderSerializer


class OrderView(ListAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class SingleOrderView(RetrieveAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    lookup_field = 'slug'


class ApplyToOrderView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request, slug):

        return Response({})


class SendApproveOrderView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request, slug):
        
        return Response({})