import mysql.connector
from django.shortcuts import render, redirect
from django.db import connection
from django.contrib import messages
from django.http import HttpResponseRedirect, JsonResponse


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

def randevu_al(request):
    return render(request, "main_app/patients/randevu_al.html")

def tibbi_raporlar_duzenle(request):
    return render(request, "main_app/patients/tibbi_raporlar_duzenle.html")

# SAYFALARI SQL İLE BAĞLAMA

baglanti = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234",
    database="prolab",
    port='3306'
)
global cursor
cursor = baglanti.cursor()

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
        
def doktor_login(request):
    if request.method == 'POST':
        username = request.POST.get('id')
        password = request.POST.get('sifre')

        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM Sifreler WHERE userID = %s AND password = %s", [username, password])
            user = cursor.fetchone()

        if user is not None:
            return render(request, "main_app/doctors/doctors_main_page.html")
        else:
            return HttpResponseRedirect('/doktor/')  # Kök URL'ye yönlendir

def doktor_patient(request):
    return render(request, "main_app/doctors/doctors_my_patients.html")


def yonetici_login(request):
    if request.method == 'POST':
        username = request.POST.get('id')
        password = request.POST.get('sifre')

        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM Sifreler WHERE userID = %s AND password = %s", [username, password])
            user = cursor.fetchone()

        if user is not None:
            return render(request, "main_app/admin/adminfirst.html")
        else:
            return HttpResponseRedirect('/yonetici/')


def admin_second_patient(request):
    if request.method == 'POST':
        action = request.POST.get('action')
        hastaid = request.POST.get('hastaid')
        hasta_ad = request.POST.get('hasta_ad')
        hasta_soyad = request.POST.get('hasta_soyad')
        hasta_dogum_tarihi = request.POST.get('hasta_dogumTarihi')
        hasta_cinsiyet = request.POST.get('hasta_cinsiyet')
        hasta_telefon = request.POST.get('hasta_telefonNo')
        hasta_adres = request.POST.get('hasta_adres')

        try:
            with connection.cursor() as cursor:
                if action == 'add':
                    messages.success(request, 'Hasta başarıyla eklendi.')
                    cursor.execute(
                        "INSERT INTO hastalar (hastaid, ad, soyad, dogumtarihi, cinsiyet, telefonnumarasi, adres) VALUES (%s, %s, %s, %s, %s, %s, %s)",
                        [hastaid, hasta_ad, hasta_soyad, hasta_dogum_tarihi, hasta_cinsiyet, hasta_telefon, hasta_adres]
                    )     
                elif action == 'update':
                    messages.success(request, 'Hasta başarıyla güncellendi.')
                    cursor.execute(
                        "UPDATE hastalar SET ad = %s, soyad = %s, dogumtarihi = %s, cinsiyet = %s, telefonnumarasi = %s, adres = %s WHERE hastaid = %s",
                        [hasta_ad, hasta_soyad, hasta_dogum_tarihi, hasta_cinsiyet, hasta_telefon, hasta_adres, hastaid]
                    )
                elif action == 'delete':
                    messages.success(request, 'Hasta başarıyla silindi.')
                    cursor.execute(
                        "DELETE FROM hastalar WHERE hastaid = %s",
                        [hastaid]
                    )
                else:
                    messages.error(request, 'Geçersiz işlem.')
        except Exception as e:
            messages.error(request, f'Bir hata oluştu: {str(e)}')

        return redirect('admin_second_patient')
    else:
        hastalar = []
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM hastalar")
            hastalar = cursor.fetchall()
        return render(request, 'main_app/admin/adminsecond_patient.html', {'hastalar': hastalar})


def admin_second_doctor(request):
    if request.method == 'POST':
        action = request.POST.get('action')
        doktorid = request.POST.get('doktorid')
        doktor_ad = request.POST.get('doktor_ad')
        doktor_soyad = request.POST.get('doktor_soyad')
        doktor_uzmanlikalani = request.POST.get('doktor_uzmanlikalani')
        doktor_calistigihastane = request.POST.get('doktor_calistigihastane')

        try:
            with connection.cursor() as cursor:
                if action == 'add':
                    cursor.execute(
                        "INSERT INTO doktorlar (doktorid, ad, soyad, uzmanlikalani, calistigihastane) VALUES (%s, %s, %s, %s, %s)",
                        [doktorid, doktor_ad, doktor_soyad, doktor_uzmanlikalani, doktor_calistigihastane]
                    )
                    messages.success(request, 'Doktor başarıyla eklendi.')
                elif action == 'update':
                    cursor.execute(
                        "UPDATE doktorlar SET ad = %s, soyad = %s, uzmanlikalani = %s, calistigihastane = %s WHERE doktorid = %s",
                        [doktor_ad, doktor_soyad, doktor_uzmanlikalani, doktor_calistigihastane, doktorid]
                    )
                    messages.success(request, 'Doktor başarıyla güncellendi.')
                elif action == 'delete':
                    cursor.execute(
                        "DELETE FROM doktorlar WHERE doktorid = %s",
                        [doktorid]
                    )
                    messages.success(request, 'Doktor başarıyla silindi.')
                else:
                    messages.error(request, 'Geçersiz işlem.')
        except Exception as e:
            messages.error(request, f'Bir hata oluştu: {str(e)}')

        return redirect('admin_second_doctor')
    else:
        doktorlar = []
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM doktorlar")
            doktorlar = cursor.fetchall()
        return render(request, 'main_app/admin/adminsecond_doctor.html', {'doktorlar': doktorlar})
    
def doctor_ekle(request):
    global cursor
    cursor.execute("SELECT DISTINCT UzmanlikAlani FROM Doktorlar")
    yeni_doktor = [row[0] for row in cursor.fetchall()]
    return JsonResponse({'yeni_doktor':yeni_doktor})

def admin_second_report(request):
    if request.method == 'POST':
        action = request.POST.get('action')
        raporid = request.POST.get('raporid')
        raportarihi = request.POST.get('raportarihi')
        raporicerigi = request.POST.get('raporicerigi')
        hastaid = request.POST.get('hastaid')
        doktorid = request.POST.get('doktorid')

        try:
            with connection.cursor() as cursor:
                if action == 'add':
                    cursor.execute(
                        "INSERT INTO tibbiraporlar (raporid, raportarihi, raporicerigi, hastaid, doktorid) VALUES (%s, %s, %s, %s, %s)",
                        [raporid, raportarihi, raporicerigi, hastaid, doktorid]
                    )
                    messages.success(request, 'Rapor başarıyla eklendi.')
                elif action == 'update':
                    cursor.execute(
                        "UPDATE tibbiraporlar SET raportarihi = %s, raporicerigi = %s, hastaid = %s, doktorid = %s WHERE raporid = %s",
                        [raportarihi, raporicerigi, hastaid, doktorid, raporid]
                    )
                    messages.success(request, 'Rapor başarıyla güncellendi.')
                elif action == 'delete':
                    cursor.execute(
                        "DELETE FROM tibbiraporlar WHERE raporid = %s",
                        [raporid]
                    )
                    messages.success(request, 'Rapor başarıyla silindi.')
                else:
                    messages.error(request, 'Geçersiz işlem.')
        except Exception as e:
            messages.error(request, f'Bir hata oluştu: {str(e)}')

        return redirect('admin_second_report')
    else:
        raporlar = []
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM tibbiraporlar")
            raporlar = cursor.fetchall()
        return render(request, 'main_app/admin/adminsecond_report.html', {'raporlar': raporlar})

def hasta_rapor_goster(request):
    hasta_id = request.GET.get('hasta_id')  # URL'den rapor_id parametresini al
    doktor_id = request.GET.get('doktor_id')  # URL'den rapor_id parametresini al
    raporlar = []
    if hasta_id and doktor_id:
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM tibbiraporlar WHERE hastaid = %s AND doktorid = %s", [hasta_id, doktor_id])
            raporlar = cursor.fetchall()
            if not raporlar:
                messages.error(request, "Rapor bulunamadı.")  # Rapor bulunamadı mesajı

    return render(request, 'main_app/admin/adminsecond_report.html', {'raporlar': raporlar})

def doktor_rapor_goster(request):
    doctor_id = request.GET.get('doctor_id')  # URL'den rapor_id parametresini al
    hasta_id = request.GET.get('hasta_id')  # URL'den rapor_id parametresini al
    raporlar = []
    if doctor_id and hasta_id:
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM tibbiraporlar WHERE doktorid = %s AND hastaid = %s", [doctor_id, hasta_id])
            raporlar = cursor.fetchall()
            if not raporlar:
                messages.error(request, "Rapor bulunamadı.")  # Rapor bulunamadı mesajı

    return render(request, 'main_app/admin/adminsecond_report.html', {'raporlar': raporlar})

def admin_second_appointment(request):
    if request.method == 'POST':
        action = request.POST.get('action')
        randevuid = request.POST.get('randevuid')
        hastaid = request.POST.get('hastaid')
        doktorid = request.POST.get('doktorid')
        tarih = request.POST.get('tarih')
        saat = request.POST.get('saat')

        with connection.cursor() as cursor:
            if action == 'update':
                cursor.execute(
                    "UPDATE randevular SET hastaid = %s, doktorid = %s, tarih = %s, saat = %s WHERE randevuid = %s",
                    [hastaid, doktorid, tarih, saat, randevuid]
                )
                messages.success(request, 'Randevu başarıyla güncellendi.')
            elif action == 'delete':
                cursor.execute(
                    "DELETE FROM randevular WHERE randevuid = %s",
                    [randevuid]
                )
                messages.success(request, 'Randevu başarıyla silindi.')
            else:
                messages.error(request, 'Geçersiz işlem.')
        return redirect('admin_second_appointment')
    else:
        randevular = []
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM randevular")
            randevular = cursor.fetchall()
        return render(request, 'main_app/admin/adminsecond_appointment.html', {'randevular': randevular})


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
    return JsonResponse({'doktorlar': doktorlar})