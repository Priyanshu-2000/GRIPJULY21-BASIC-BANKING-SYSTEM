from django.urls import path
from bank import views

urlpatterns = [
        path('',views.AboutView.as_view(),name = 'about' ),
        path('about/', views.AboutView.as_view(),name = 'about'),
        path('customers/', views.CustomerListView.as_view(),name = 'customer_list'),
        path('transfer_list/', views.TransactionListView.as_view(), name = 'transfer_list'),
        path('transaction/', views.Transfer, name = 'transaction'),
        path('transaction/transfer_list', views.TransactionListView.as_view(), name = 'transfer_list'),
        path('customers/new', views.CustomerCreateView.as_view(), name = 'customer_new'),

]
