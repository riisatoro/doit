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


class StockOrderView(APIView):

    def get(self, slug):
        return Response({})
