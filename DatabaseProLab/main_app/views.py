from django.shortcuts import render, redirect
from django.db import connection
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.template import loader
from .models import Doktorlar
from .models import Hastalar
from .models import Yonetici

def home(request):
    return render(request, "main_app/mainpage.html")

def admin(request):
    return render(request, "main_app/admin/admin.html")

def admin_first(request):
    return render(request, "main_app/admin/adminfirst.html")

def doctors(request):
    return render(request, "main_app/doctors/doctors.html")

def patients(request):
    return render(request, "main_app/patients/patients.html")

# SAYFALARI SQL İLE BAĞLAMA

def patient_login(request):
    if request.method == 'POST':
        username = request.POST.get('id')
        password = request.POST.get('sifre')

        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM Sifreler WHERE userID = %s AND password = %s", [username, password])
            user = cursor.fetchone()

        if user is not None:
            return render(request, "main_app/patients/patients_main_page.html")
        else:
            return HttpResponseRedirect('/hasta/')  # Kök URL'ye yönlendir

def admin_second_patient(request):
    return render(request, 'main_app/admin/adminsecond_patient.html')

def admin_second_doctor(request):
    return render(request, 'main_app/admin/adminsecond_doctor.html')

def admin_second_report(request):
    return render(request, 'main_app/admin/adminsecond_report.html')

def yonetici_login(request):
    if request.method == 'POST':
        username = request.POST.get('id')
        password = request.POST.get('yoneticisifre')

        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM Yonetici WHERE YoneticiID = %s AND yonetici_sifre = %s", [username, password])
            user = cursor.fetchone()

        if user is not None:
            return render(request, "main_app/patients/patients_main_page.html")
        else:
            return HttpResponseRedirect('/yonetici/giris/')

