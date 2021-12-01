from rest_framework.permissions import IsAuthenticated 
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK

from app_utils.forms import RegistrationForm
from app_utils.models import CustomUser
from app_utils.serializers import PrivateUserProfileSerializer, PublicUserProfileSerializer
from app_utils.services.cloudinary import upload_avatar


class UserProfile(APIView): 
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        data = PrivateUserProfileSerializer(request.user).data
        return Response(data, status=HTTP_200_OK)

    def post(self, request):
        avatar_data = upload_avatar(request.FILES.get('avatar'), request.user)
        about = request.data.get('about')
        CustomUser.objects.filter(id=request.user.id).update(
            about=about, avatar=avatar_data['url'], avatar_id=avatar_data['media_id']
        )
        return Response({}, status=HTTP_200_OK)


class PublicProfile(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, user_slug):
        user = CustomUser.objects.filter(slug=user_slug).first()
        data = PublicUserProfileSerializer(user).data
        return Response(data, status=HTTP_200_OK)

