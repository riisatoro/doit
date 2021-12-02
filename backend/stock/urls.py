from django.urls import path
from stock.views import (
    StockOrderView,
    StockOrderListView,
    ApplyToOrderView,
    SubmitSolutionView,
    ConfirmApplicantView,
    ConfirmFinishOrderView,
    StockOrderArchiveView,
)

urlpatterns = [
    path('', StockOrderListView.as_view(), name='all_orders'),
    
    path('my/', StockOrderArchiveView.as_view(), name='my_archive'),
    path('new/', StockOrderView.as_view(), name='create_order'),
    path('edit/', StockOrderView.as_view(), name='edit_order'),

    path('apply/', ApplyToOrderView.as_view(), name='apply_order'),
    path('add/solution/', SubmitSolutionView.as_view(), name='submit_solution'),
    path('confirm/applicant/', ConfirmApplicantView.as_view(), name='confirm_applicant'),
    path('confirm/finished/', ConfirmFinishOrderView.as_view(), name='confirm_finished'),

    path('<slug:slug>/', StockOrderView.as_view(), name='order_details'),

]
