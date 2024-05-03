from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="mainpage"),
    path("yonetici/", views.admin, name="admin"),
    path("yonetici/giris/", views.admin_first, name="admin_first"),
    path("doktor/", views.doctors, name="doctors"),
    path("hasta/", views.patients, name="patients"),
]
