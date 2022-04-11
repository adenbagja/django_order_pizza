from django.urls import path
from . import views

urlpatterns = [
    path('cek_loc', views.ip, name="cek_loc"),
]