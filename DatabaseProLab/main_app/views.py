from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from .models import Doktorlar

def home(request):
    return render(request, "main_app/mainpage.html")

def admin(request):
    return render(request, "main_app/admin/admin.html")

def admin_first(request):
    '''mydata = Member.objects.all()
    context = {
        'mymembers': mydata,
    }'''
    return render(request, "main_app/admin/adminfirst.html", '''context''')

def doctors(request):
    return render(request, "main_app/doctors/doctors.html")

def patients(request):
    return render(request, "main_app/patients/patients.html")
