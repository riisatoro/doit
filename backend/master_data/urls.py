from django.urls import path
from .views import (
    UserTypeView,
)

urlpatterns = [
    path('usertype/', UserTypeView.as_view(), name='registration'),
]
