from django.shortcuts import get_object_or_404
from django.db.models import Q
from rest_framework.views import APIView, Response
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.status import HTTP_400_BAD_REQUEST

from app_utils.models import Order, OrderApplicant
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
        order = get_object_or_404(Order, slug=slug)
        applied_order = OrderApplicant.objects.filter(applicant=request.user, order=order).first()
        if applied_order:
            return Response({'detail': 'Already applied'}, status=HTTP_400_BAD_REQUEST)
        
        OrderApplicant.objects.create(applicant=request.user, order=order)
        return Response({'detail': 'ok'})


class SendApproveOrderView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request, slug):
        
        return Response({})