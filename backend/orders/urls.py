from django.contrib import admin
from django.urls import path
from django.urls.conf import include

from orders.views import OrderView, ApplyToOrderView, SendApproveOrderView

urlpatterns = [
    path('', OrderView.as_view(), name='orders'),
    path('<slug:slug>/assign/', ApplyToOrderView.as_view(), name='assing_order'),
    path('<slug:slug>/approve/', SendApproveOrderView.as_view(), name='approve_order'),
]
