from django.urls import path
from . import views

urlpatterns = [
    path('cek_loc', views.scrap, name="cek_loc"),
    path('orders', views.orders, name="orders"),
]