from rest_framework import status
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, get_object_or_404
from rest_framework.response import Response
from rest_framework.status import (
    HTTP_200_OK,
    HTTP_201_CREATED,
    HTTP_400_BAD_REQUEST,
    HTTP_401_UNAUTHORIZED,
)
from rest_framework.permissions import IsAuthenticated

from app_utils.models import (
    StockOrder,
    OrderStatus,
    StockOrderApplicant,
)
from app_utils.serializers import (
    OrderListSerializer,
    OrderDetailSerializer,
    StockOrderApplicantSerializer,
)


class StockOrderListView(ListAPIView):
    serializer_class = OrderListSerializer
    permission_classes = (IsAuthenticated,)
    queryset = StockOrder.objects.filter(order_status=OrderStatus.OPEN)


class StockOrderView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, slug):
        order = get_object_or_404(StockOrder, slug=slug)
        data = OrderDetailSerializer(order).data

        if order.author == request.user:
            applicants = StockOrderApplicant.objects.filter(order=order.id)
            data['applicants'] = StockOrderApplicantSerializer(applicants, many=True).data

        return Response(data)


class ApplyToOrderView(APIView):
    permission_classes = (IsAuthenticated,)


class SubmitSolutionView(APIView):
    permission_classes = (IsAuthenticated,)


class ConfirmApplicantView(APIView):
    permission_classes = (IsAuthenticated,)


class ConfirmFinishOrderView(APIView):
    permission_classes = (IsAuthenticated,)
    

class StockOrderArchiveView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        user = request.user
        
        my_orders = StockOrder.objects.filter(author=user)
        applied_order = StockOrder.objects.filter(applicants__in=[user])
        in_progress = StockOrder.objects.filter(executor=user).exclude(order_status=OrderStatus.FINISHED)
        executed_orders = StockOrder.objects.filter(executor=user, order_status=OrderStatus.FINISHED)

        data = {
            'my': OrderListSerializer(my_orders, many=True).data,
            'applied': OrderListSerializer(applied_order, many=True).data,
            'in_progress': OrderListSerializer(in_progress, many=True).data,
            'executed': OrderListSerializer(executed_orders, many=True).data,
        }
        return Response(data)