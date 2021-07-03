from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import (
    HTTP_201_CREATED,
    HTTP_400_BAD_REQUEST,
)
from payload_forms import RegistrationForm
from emails.send import send_email


class Registration(APIView):
    def post(self, request):
        user = RegistrationForm(request.data)
        if not user.is_valid():
            return Response({'details': user.errors.as_data()}, status=HTTP_400_BAD_REQUEST)
        user = user.save()
        send_email(recepients=[user.email])
        return Response({}, status=HTTP_201_CREATED)