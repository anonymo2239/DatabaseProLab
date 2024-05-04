from django.shortcuts import render

def home(request):
    return render(request, "mainpage.html")

def admin(request):
    return render(request, "admin/admin.html")

def admin_first(request):
    return render(request, "admin/adminfirst.html")

def doctors(request):
    return render(request, "doctors/doctors.html")

def patients(request):
    return render(request, "patients/patients.html")
