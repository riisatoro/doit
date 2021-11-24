from os import stat
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import (
    HTTP_200_OK,
    HTTP_201_CREATED,
    HTTP_400_BAD_REQUEST,
    HTTP_401_UNAUTHORIZED,
)
from payload_forms import RegistrationForm
from services.mailgun import send_email
from encoder import (
    encode_email_token,
    decode_email_token,
)
from db_models.models import CustomUser


class Registration(APIView):
    def post(self, request):
        user = RegistrationForm(request.data)
        if not user.is_valid():
            return Response({'detail': user.errors.as_data()}, status=HTTP_400_BAD_REQUEST)
        user = user.save()
        send_email(recepients=[user.email], token=encode_email_token(user.email))
        return Response(
            {'detail': 'You have registered successfully'},
            status=HTTP_201_CREATED
        )


class Confirmation(APIView):
    def get(self, request, token):
        try:
            email = decode_email_token(token)
        except ValueError:
            return Response({'detail': 'Token is invalid or expired'}, status=HTTP_401_UNAUTHORIZED)
        user = CustomUser.objects.filter(email=email).first()
        if not user:
            return Response({'detail': 'Token is invalid or expired'}, status=HTTP_401_UNAUTHORIZED)
        user.is_active = True
        user.save()
        return Response({'detail': 'Your have confirmed your account successfully'}, status=HTTP_200_OK)
