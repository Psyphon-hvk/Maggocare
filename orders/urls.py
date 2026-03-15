from django.urls import path
from . import views

urlpatterns = [
    path('order/', views.order_start, name='order_start'),
    path('success/', views.order_success, name='order_success'),
]