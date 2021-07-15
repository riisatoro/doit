from rest_framework.permissions import IsAuthenticated 
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import (
    HTTP_200_OK,
)
from payload_forms import RegistrationForm
from db_models.models import CustomUser

from servises.cloudinary import upload_avatar


class UserProfile(APIView): 
    permission_classes = [IsAuthenticated,]

    def get(self, request):
        return Response({}, status=HTTP_200_OK)

    def post(self, request):
        avatar_data = upload_avatar(request.FILES.get('avatar'), request.user)
        about = request.data.get('about')
        CustomUser.objects.filter(id=request.user.id).update(
            about=about, avatar=avatar_data['url'], avatar_id=avatar_data['media_id']
        )
        return Response({}, status=HTTP_200_OK)
