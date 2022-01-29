from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK

from app_utils.serializers import UserDetailsSerializer
from app_utils.models import CustomUser


class UserDetailsView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        user_data = UserDetailsSerializer(request.user).data
        return Response(user_data, status=HTTP_200_OK)