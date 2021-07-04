from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from .views import (
    Registration,
    Confirmation,
)

urlpatterns = [
    path('register/', Registration.as_view(), name='registration'),
    path('confirm/<str:token>/', Confirmation.as_view(), name='confirmation'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
