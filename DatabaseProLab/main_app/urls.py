from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

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
    path("doktor/anasayfa/", views.doktor_login, name="doktor_login"),
    path("doktor/anasayfa/hastalarim", views.doktor_patient, name="doktor_patient"),
    path("hasta/", views.patients, name="patients"),
    path("hasta/anasayfa/", views.patient_login, name="patient_login"),
    path("hasta/anasayfa/randevual", views.randevu_al, name="randevu_al"),
    path("hasta/anasayfa/tibbi_raporlar_duzenle", views.tibbi_raporlar_duzenle, name="tibbi_raporlar_duzenle"),
    path("get_uzmanliklar/", views.get_uzmanliklar, name="get_uzmanliklar"),
    path("get_hastaneler/", views.get_hastaneler, name="get_hastaneler"),
    path("get_doktorlar/", views.get_doktorlar, name="get_doktorlar"),
    path("randevu_ekle/", views.randevu_ekle, name="randevu_ekle"),
    path("doctor_ekle/", views.doctor_ekle, name="doctor_ekle"),
    path('hasta-rapor-goster/', views.hasta_rapor_goster, name='hasta_rapor_goster'),
    path('doktor-rapor-goster/', views.doktor_rapor_goster, name='doktor_rapor_goster'),
] 

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

