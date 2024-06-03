from django.urls import path
from products import views as product_views
from orders import views as order_views  # Импортируем представления из модуля orders

app_name = 'products'
urlpatterns = [
    path('', product_views.home_page, name='index'),
    path('products/<slug:slug>/', product_views.detail_page, name='detail'),
    path('products/<slug:slug>/reviews/<int:id>/', product_views.delete_review, name='delete_review'),
    path('products/<slug:slug>/edit_review/<int:id>/', product_views.edit_review, name='edit_review'),
    path('create-product/', product_views.create_product, name='create_product'),
    # path('orders/', order_views.orders_list, name='orders_list'),  # Указываем на представление orders_list из модуля orders
]
