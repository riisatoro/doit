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

    def get(self, request, slug):
        order = get_object_or_404(StockOrder, slug=slug)
        data = OrderDetailSerializer(order).data

        if order.author == request.user:
            applicants = StockOrderApplicant.objects.filter(order=order.id)
            data['applicants'] = StockOrderApplicantSerializer(applicants, many=True).data

        return Response(data)


class ApplyToOrderView(APIView):
    ...


class SubmitSolutionView(APIView):
    ...


class ConfirmApplicantView(APIView):
    ...


class ConfirmFinishOrderView(APIView):
    ...


class StockOrderArchiveView(APIView):
    ...