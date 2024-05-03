from django.shortcuts import render

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
