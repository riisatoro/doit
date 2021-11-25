from django.urls import path
from .views import (
    UserProfile,
    PublicProfile,
)

urlpatterns = [
    path('profile/', UserProfile.as_view(), name='profile'),
    path('profile/<str:user_slug>/', PublicProfile.as_view(), name='profile'),
]
