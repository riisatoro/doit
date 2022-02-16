from cmath import pi
from functools import reduce
import operator
from django.shortcuts import get_object_or_404
from django.db.models import Q
from rest_framework.views import APIView, Response
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.status import HTTP_400_BAD_REQUEST

from app_utils.models import Order, OrderApplicant, MediaStorage, OrderTag
from app_utils.serializers import OrderSerializer
from app_utils.services.cloudinary import upload_media


class OrderView(ListAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = OrderSerializer

    def list(self, request):
        search_tags = request.query_params.getlist('tags')
        queryset = Order.objects.exclude(applicants=request.user).order_by('-created_at')

        if search_tags:
            tags_query = OrderTag.objects.filter(reduce(operator.and_, [Q(title__icontains=tag) for tag in search_tags]))
            queryset = queryset.filter(tags__in=tags_query)
            

        items = self.serializer_class(queryset, many=True)
        pinned = Order.objects.filter(applicants=self.request.user).order_by('-created_at')
        pinned = self.serializer_class(pinned, many=True)
        
        return Response({'pinned': pinned.data, 'list': items.data})


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


class RemoveFromOrderView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request, slug):
        order = get_object_or_404(Order, slug=slug)
        OrderApplicant.objects.filter(applicant=request.user, order=order).delete()
        return Response({'detail': 'ok'})


class SendApproveOrderView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request, slug):
        order = get_object_or_404(Order, slug=slug)
        application = get_object_or_404(OrderApplicant, order=order, applicant=request.user)
        if application.review_required():
            return Response({'detail': 'You already submited a media files'}, status=HTTP_400_BAD_REQUEST)

        for file in request.FILES.getlist('file'):
            instance = MediaStorage.objects.create(title=file.name, document=file, content_type=file.content_type)
            application.media.add(instance)
        return Response({'detail': 'ok'})
