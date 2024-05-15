from django.shortcuts import render, redirect
from django.db import connection
from django.contrib import messages
from django.http import HttpResponseRedirect, JsonResponse
import mysql.connector
from mysql.connector import Error

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

def randevu_al(request):
    return render(request, "patients/randevu_al.html")

def tibbi_raporlar_duzenle(request):
    return render(request, "patients/tibbi_raporlar_duzenle.html")

baglanti = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234",
    database="prolab"
)
global cursor
cursor = baglanti.cursor()

def hasta_kayit(request):
    if request.method == 'POST':
        ad = request.POST.get('ad')
        soyad = request.POST.get('soyad')
        dogum_tarihi = request.POST.get('dogum_tarihi')
        cinsiyet = request.POST.get('cinsiyet')
        telefon = request.POST.get('telefon_numarasi')
        adres = request.POST.get('adres')

        with connection.cursor() as cursor:
            cursor.execute(
                "INSERT INTO Hastalar (Ad, Soyad, DogumTarihi, Cinsiyet, TelefonNumarasi, Adres) VALUES (%s, %s, %s, %s, %s, %s)",
                [ad, soyad, dogum_tarihi, cinsiyet, telefon, adres]
            )

        messages.success(request, 'Hasta başarıyla kaydedildi.')
        return redirect('hasta_kayit')
    else:
        return render(request, 'hasta_kayit.html')

def patient_login(request):
    global cursor
    if request.method == 'POST':
        username = request.POST.get('id')
        password = request.POST.get('sifre')


        cursor.execute("SELECT * FROM Sifreler WHERE UserID = %s AND Password = %s", [username, password])
        user = cursor.fetchone()

        if user is not None:
            request.session['user_id'] = username
            cursor.execute("SELECT RandevuID, DoktorID, Tarih, Saat FROM Randevular WHERE HastaID = %s", [username])
            randevular = cursor.fetchall()

            context = {
                'randevular': randevular
            }

            return render(request, "patients/patients_main_page.html", context)
        else:
            messages.error(request, 'Geçersiz kullanıcı adı veya şifre.')
            return redirect('/hasta/')

def admin_second_patient(request):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM Hastalar")
        hastalar = cursor.fetchall()
    return render(request, 'admin/adminsecond_patient.html', {'hastalar': hastalar})

def admin_second_doctor(request):
    if request.method == 'POST':
        action = request.POST.get('action')

        if action == 'add':
            doktorid = request.POST.get('doktorid')
            doktor_ad = request.POST.get('doktor_ad')
            doktor_soyad = request.POST.get('doktor_soyad')
            doktor_uzmanlikalani = request.POST.get('doktor_uzmanlikalani')
            doktor_calistigihastane = request.POST.get('doktor_calistigihastane')

            with connection.cursor() as cursor:
                cursor.execute("SELECT * FROM Doktorlar WHERE DoktorID = %s", [doktorid])
                row = cursor.fetchone()

                if row is None:
                    cursor.execute(
                        "INSERT INTO Doktorlar (DoktorID, Ad, Soyad, UzmanlikAlani, CalistigiHastane) VALUES (%s, %s, %s, %s, %s)",
                        [doktorid, doktor_ad, doktor_soyad, doktor_uzmanlikalani, doktor_calistigihastane]
                    )
                    messages.success(request, 'Doktor başarıyla eklendi.')
                else:
                    messages.error(request, 'Bu ID ile zaten bir doktor mevcut.')

        elif action == 'update':
            doktorid = request.POST.get('doktorid')
            doktor_ad = request.POST.get('doktor_ad')
            doktor_soyad = request.POST.get('doktor_soyad')
            doktor_uzmanlikalani = request.POST.get('doktor_uzmanlikalani')
            doktor_calistigihastane = request.POST.get('doktor_calistigihastane')

            with connection.cursor() as cursor:
                cursor.execute("SELECT * FROM Doktorlar WHERE DoktorID = %s", [doktorid])
                row = cursor.fetchone()

                if row is not None:
                    cursor.execute(
                        "UPDATE Doktorlar SET Ad = %s, Soyad = %s, UzmanlikAlani = %s, CalistigiHastane = %s WHERE DoktorID = %s",
                        [doktor_ad, doktor_soyad, doktor_uzmanlikalani, doktor_calistigihastane, doktorid]
                    )
                    messages.success(request, 'Doktor başarıyla güncellendi.')
                else:
                    messages.error(request, 'Bu ID ile bir doktor bulunamadı.')

        elif action == 'delete':
            doktorid = request.POST.get('doktorid')

            with connection.cursor() as cursor:
                cursor.execute("SELECT * FROM Doktorlar WHERE DoktorID = %s", [doktorid])
                row = cursor.fetchone()

                if row is not None:
                    cursor.execute("DELETE FROM Doktorlar WHERE DoktorID = %s", [doktorid])
                    messages.success(request, 'Doktor başarıyla silindi.')
                else:
                    messages.error(request, 'Bu ID ile bir doktor bulunamadı.')

        elif action == 'select':
            doktorid = request.POST.get('doktorid')

            with connection.cursor() as cursor:
                cursor.execute("SELECT * FROM Doktorlar WHERE DoktorID = %s", [doktorid])
                row = cursor.fetchone()

                if row is not None:
                    messages.success(request, f'Doktor bulundu: {row}')
                else:
                    messages.error(request, 'Bu ID ile bir doktor bulunamadı.')

        return redirect('admin_second_doctor')

    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM Doktorlar")
        doktorlar = cursor.fetchall()
    return render(request, 'admin/adminsecond_doctor.html', {'doktorlar': doktorlar})

def admin_second_report(request):
    return render(request, 'admin/adminsecond_report.html')

def admin_second_appointment(request):
    return render(request, 'admin/adminsecond_appointment.html')

def yonetici_login(request):
    if request.method == 'POST':
        username = request.POST.get('id')
        password = request.POST.get('yoneticisifre')

        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM Yonetici WHERE YoneticiID = %s AND yonetici_sifre = %s", [username, password])
            user = cursor.fetchone()

        if user is not None:
            return render(request, "admin/adminfirst.html")
        else:
            messages.error(request, 'Geçersiz kullanıcı adı veya şifre.')
            return redirect('/yonetici/giris/')

    return render(request, 'admin/adminfirst.html')

def randevu_ekle(request):
    global cursor
    if request.method == 'POST':
        doktor_id = request.POST.get('doktor_id')
        tarih = request.POST.get('tarih')
        saat = request.POST.get('saat')
        hasta_id = request.session.get('user_id')
        if doktor_id and hasta_id and tarih and saat:
            cursor.execute("INSERT INTO Randevular (HastaID, DoktorID, Tarih, Saat) VALUES (%s, %s, %s, %s)",
                           [hasta_id, doktor_id, tarih, saat])
            baglanti.commit()
            return JsonResponse({'success': True})
        else:
            return JsonResponse({'success': False, 'message': 'Tüm alanlar doldurulmalıdır.'})
    return render(request, 'patients/randevu_al.html')

def get_uzmanliklar(request):
    global cursor
    cursor.execute("SELECT DISTINCT UzmanlikAlani FROM Doktorlar")
    uzmanliklar = [row[0] for row in cursor.fetchall()]
    return JsonResponse({'uzmanliklar': uzmanliklar})

def get_hastaneler(request):
    global cursor
    uzmanlik = request.GET.get('uzmanlik')
    cursor.execute("SELECT DISTINCT CalistigiHastane FROM Doktorlar WHERE UzmanlikAlani = %s", [uzmanlik])
    hastaneler = [row[0] for row in cursor.fetchall()]
    return JsonResponse({'hastaneler': hastaneler})

def get_doktorlar(request):
    global cursor
    hastane = request.GET.get('hastane')
    cursor.execute("SELECT DoktorID, CONCAT(Ad, ' ', Soyad) AS AdSoyad FROM Doktorlar WHERE CalistigiHastane = %s", [hastane])
    doktorlar = [{'id': row[0], 'ad_soyad': row[1]} for row in cursor.fetchall()]
    return JsonResponse({'doktorlar': doktorlar})
