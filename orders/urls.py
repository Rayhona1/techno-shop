from django.urls import path
from .views import create_order, all_orders
app_name = 'orders'
urlpatterns = [
    path('create-order/<slug:slug>', create_order, name='create_order'),
    path('orders/', all_orders, name='all-orders'),
    path('my-orders/', all_orders, name='my-orders')
]