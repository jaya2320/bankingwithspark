from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('index',views.index,name='index'),
    path('customer',views.customer,name='customer'),
    path('transaction/<int:pk>',views.transaction,name='transaction'),
    path('transaction_history/<int:pk2>',views.transaction_history,name='transaction_history'),
    path('make_transaction/index',views.index,name='index'),
    path('make_transaction/<int:pk1>',views.make_transaction,name='make_transaction'),
    path('delete_history/<int:pk3>',views.delete_history,name="delete_history"),
    path('delete_customer/<int:pk3>',views.delete_customer,name="delete_customer")
   
]