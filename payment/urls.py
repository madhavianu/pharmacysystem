from django.urls import path
from . import views

urlpatterns=[
    path('createpayment/', views.create_payment, name = 'create_payment'),
    #path('paysuccess/', views.payment_success, name = 'payment_success'),
    path('transactionlist/', views.transaction_list, name = 'transaction_list'),
    
    ]