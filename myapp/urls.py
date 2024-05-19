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
    path('yonetici/giris/anasayfa/raporedit/post', views.admin_second_report_post, name='admin_second_report_post'),
    path('yonetici/giris/anasayfa/randevuedit', views.admin_second_appointment, name='admin_second_appointment'),
    path('yonetici/giris/anasayfa/randevuedit/post', views.admin_second_appointment_post, name='admin_second_appointment_post'),
    path('yonetici/giris/anasayfa/randevuedit/search', views.admin_search_appointments, name='admin_search_appointments'),
    path("doktor/", views.doctors, name="doctors"),
    path("doktor/anasayfa/", views.doktor_login, name="doktor_login"),
    path("doktor/anasayfa/hastalarim", views.doktor_patient, name="doktor_patient"),
    path('hasta/', views.patients, name='patients'),
    path("hasta/anasayfa/", views.patient_login, name="patient_login"),
    path('hasta/kayit/', views.patient_new_user, name='patient_register'),
    path("hasta/anasayfa/randevual", views.randevu_al, name="randevu_al"),
    path("hasta/anasayfa/raporlar", views.patient_reports, name="patient_report"),
    path("get_uzmanliklar/", views.get_uzmanliklar, name="get_uzmanliklar"),
    path("get_hastaneler/", views.get_hastaneler, name="get_hastaneler"),
    path("get_doktorlar/", views.get_doktorlar, name="get_doktorlar"),
    path("randevu_ekle/", views.randevu_ekle, name="randevu_ekle"),
    path("search_appointments/", views.search_appointments, name="search_appointments"),
    path("doctor_ekle/", views.doctor_ekle, name="doctor_ekle"),
    path("search_reports/", views.search_reports, name="search_reports"),
    path("edit_report/", views.edit_report, name="edit_report"),
    path("add_or_update_report/", views.add_or_update_report, name="add_or_update_report"),
    path("search_patients/", views.search_patients, name="search_patients"),
    path("search_doctors/", views.search_doctors, name="search_doctors"),
    path("get_doctor_appointments/", views.get_doctor_appointments, name="get_doctor_appointments"),
    path("get_doctor_patients/", views.get_doctor_patients, name="get_doctor_patients"),
    path("get_patient_reports/", views.get_patient_reports, name="get_patient_reports"),
    path('doktor/rapor-ekle/', views.add_or_update_report, name='add_or_update_report'),
    path("delete_report/", views.delete_report, name="delete_report"),
    path("register_patient/", views.register_patient, name="register_patient"),
    path("delete_appointment/", views.delete_appointment, name="delete_appointment"),
    path('doktor/anasayfa/rapor-ekle/', views.add_or_update_report_page, name='add_or_update_report_page'),
    path("get_notifications/", views.get_notifications, name="get_notifications"),  # Yeni eklendi
    path('reports/<int:report_id>/', views.show_report, name='show_report'),
    path("mark_notifications_as_read/", views.mark_notifications_as_read, name="mark_notifications_as_read"),  # Yeni eklendi
]
