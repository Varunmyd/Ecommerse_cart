
from django.urls import path

from cart import views

app_name = 'cart'

urlpatterns = [
    path('add/<int:product_id>/', views.add_cart, name='add_cart'),
    path('cartt', views.cart_detail, name='cart_detail'),
    path('minus/<int:product_id>/', views.minus_cart, name='minus_cart'),
    path('remove/<int:product_id>/', views.full_remove, name='full_remove'),
    path('payment', views.payment, name='payment'),
    path('ordersuccessful', views.ordersuccess, name='ordersuccess'),
]