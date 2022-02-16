from django.contrib import admin
from django.urls import path
from django.urls.conf import include

from orders.views import (
    OrderView, 
    ApplyToOrderView, 
    SendApproveOrderView,
    SingleOrderView,
    RemoveFromOrderView,
)

urlpatterns = [
    path('', OrderView.as_view(), name='orders'),
    path('<slug:slug>/', SingleOrderView.as_view(), name='order_details'),
    path('<slug:slug>/pin/', ApplyToOrderView.as_view(), name='pin_order'),
    path('<slug:slug>/unpin/', RemoveFromOrderView.as_view(), name='unpin_order'),
    path('<slug:slug>/approve/', SendApproveOrderView.as_view(), name='approve_order'),
]
