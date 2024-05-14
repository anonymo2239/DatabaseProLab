from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="mainpage"),
    path("yonetici/", views.admin, name="admin"),
    path("yonetici/giris/", views.admin_first, name="admin_first"),
    path("yonetici/giris/anasayfa/", views.yonetici_login, name="yonetici_login"),
    path('yonetici/giris/anasayfa/hastaedit', views.admin_second_patient, name='admin_second_patient'),
    path('yonetici/giris/anasayfa/doktoredit', views.admin_second_doctor, name='admin_second_doctor'),
    path('yonetici/giris/anasayfa/raporedit', views.admin_second_report, name='admin_second_report'),
    path('yonetici/giris/anasayfa/randevuedit', views.admin_second_appointment, name='admin_second_appointment'),
    path("doktor/", views.doctors, name="doctors"),
    path("hasta/", views.patients, name="patients"),
    path("hasta/anasayfa/", views.patient_login, name="patient_login"),
    path("hasta/anasayfa/randevual", views.randevu_al, name="randevu_al"),
    path("hasta/anasayfa/tibbi_raporlar_duzenle", views.tibbi_raporlar_duzenle, name="tibbi_raporlar_duzenle"),
]