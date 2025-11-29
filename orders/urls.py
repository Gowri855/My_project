from django.urls import path
from . import views

urlpatterns = [
    path('checkout/', views.checkout_view, name='checkout'),
    path('payment/<int:order_id>/', views.payment_view, name='payment'),
    path('success/<int:order_id>/', views.order_success_view, name='order_success'),
    path('my-orders/', views.my_orders_view, name='my_orders'),
]
