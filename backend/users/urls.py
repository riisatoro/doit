from django.urls import path
from users.views import UserDetailsView

urlpatterns = [
    path('', UserDetailsView.as_view(), name='profile'),
    path('<slug:slug>/', UserDetailsView.as_view(), name='profile'),
]