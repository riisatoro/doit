from django.contrib import admin
from django.urls import path
from django.urls.conf import include

from orders.views import (
    OrderView, 
    ApplyToOrderView, 
    SendApproveOrderView,
    SingleOrderView,
)

urlpatterns = [
    path('', OrderView.as_view(), name='orders'),
    path('<slug:slug>/', SingleOrderView.as_view(), name='order_details'),
    path('<slug:slug>/assign/', ApplyToOrderView.as_view(), name='assing_order'),
    path('<slug:slug>/approve/', SendApproveOrderView.as_view(), name='approve_order'),
]
