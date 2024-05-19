from django.shortcuts import render, redirect
from django.db import connection
from django.contrib import messages
from django.http import JsonResponse
import mysql.connector
from mysql.connector import Error
import random

from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import JsonResponse
import random
from .hasta import Hasta
from .doktor import Doktor
from .randevu import Randevu
from .tibbirapor import TibbiRapor
import mysql.connector
from mysql.connector import Error

# Global connection and cursor
baglanti = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234",
    database="prolab"
)
cursor = baglanti.cursor()

def home(request):
    return render(request, "mainpage.html")

def admin(request):
    return render(request, "admin/admin.html")

def admin_first(request):
    return render(request, "admin/adminfirst.html")

def admin_second_appointment(request):
    return render(request, "admin/adminsecond_appointment.html")

def doctors(request):
    return render(request, "doctors/doctors.html")

def patients(request):
    return render(request, "patients/patients.html")

def randevu_al(request):
    return render(request, "patients/randevu_al.html")

def tibbi_raporlar_duzenle(request):
    return render(request, "patients/tibbi_raporlar_duzenle.html")

def admin_second_report(request):
    return render(request, 'admin/adminsecond_report.html')

def doktor_patient(request):
    return render(request, "doctors/doctors_my_patients.html")

def add_or_update_report_page(request):
    return render(request, "doctors/doctor_add_report.html")

def patient_new_user(request):
    return render(request, "patients/patient_new_user.html")

def patient_login(request):
    if request.method == 'POST':
        username = request.POST.get('id')
        password = request.POST.get('sifre')

        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM Sifreler WHERE UserID = %s AND Password = %s", [username, password])
            user = cursor.fetchone()

            if user:
                request.session['user_id'] = username
                cursor.execute("SELECT RandevuID, DoktorID, Tarih, Saat FROM Randevular WHERE HastaID = %s", [username])
                randevular = cursor.fetchall()

                context = {'randevular': randevular}
                return render(request, "patients/patients_main_page.html", context)
            else:
                messages.error(request, 'Geçersiz kullanıcı adı veya şifre.')
                return redirect('/hasta/')

def patient_reports(request):
    user_id = request.session.get('user_id')
    if not user_id:
        return redirect('/hasta/')

    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT RaporID, RaporTarihi, RaporIcerigi, HastaID, DoktorID
            FROM TibbiRaporlar
            WHERE HastaID = %s
        """, [user_id])
        raporlar = cursor.fetchall()

    context = {'raporlar': raporlar}
    return render(request, 'patients/patient_report.html', context)

def admin_second_patient(request):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM Hastalar")
        hastalar = cursor.fetchall()
    return render(request, 'admin/adminsecond_patient.html', {'hastalar': hastalar})

def admin_second_doctor(request):
    if request.method == 'POST':
        action = request.POST.get('action')
        doktor_id = request.POST.get('doktorid')
        doktor_ad = request.POST.get('doktor_ad')
        doktor_soyad = request.POST.get('doktor_soyad')
        doktor_uzmanlikalani = request.POST.get('doktor_uzmanlikalani')
        doktor_calistigihastane = request.POST.get('doktor_calistigihastane')

        doktor = Doktor(doktor_id, doktor_ad, doktor_soyad, doktor_uzmanlikalani, doktor_calistigihastane)

        try:
            if action == 'add':
                doktor.kaydet()
                messages.success(request, 'Doktor başarıyla eklendi.')
            elif action == 'update':
                doktor.guncelle()
                messages.success(request, 'Doktor başarıyla güncellendi.')
            elif action == 'delete':
                doktor.sil()
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
        return render(request, 'admin/adminsecond_doctor.html', {'doktorlar': doktorlar})

def randevu_ekle(request):
    if request.method == 'POST':
        doktor_id = request.POST.get('doktor_id')
        tarih = request.POST.get('tarih')
        saat = request.POST.get('saat')
        hasta_id = request.session.get('user_id')
        randevu_id = random.randint(100000, 999999)

        randevu = Randevu(randevu_id, hasta_id, doktor_id, tarih, saat)

        try:
            randevu.kaydet()
            return JsonResponse({'success': True})
        except Exception as e:
            return JsonResponse({'success': False, 'message': 'Bir hata oluştu: ' + str(e)})
    return render(request, 'patients/randevu_al.html')

def get_uzmanliklar(request):
    with connection.cursor() as cursor:
        cursor.execute("SELECT DISTINCT UzmanlikAlani FROM Doktorlar")
        uzmanliklar = [row[0] for row in cursor.fetchall()]
    return JsonResponse({'uzmanliklar': uzmanliklar})

def get_hastaneler(request):
    uzmanlik = request.GET.get('uzmanlik')
    with connection.cursor() as cursor:
        cursor.execute("SELECT DISTINCT CalistigiHastane FROM Doktorlar WHERE UzmanlikAlani = %s", [uzmanlik])
        hastaneler = [row[0] for row in cursor.fetchall()]
    return JsonResponse({'hastaneler': hastaneler})

def get_doktorlar(request):
    hastane = request.GET.get('hastane')
    with connection.cursor() as cursor:
        cursor.execute("SELECT DoktorID, CONCAT(Ad, ' ', Soyad) AS AdSoyad FROM Doktorlar WHERE CalistigiHastane = %s", [hastane])
        doktorlar = [{'id': row[0], 'ad_soyad': row[1]} for row in cursor.fetchall()]
    return JsonResponse({'doktorlar': doktorlar})

def yonetici_login(request):
    if request.method == 'POST':
        username = request.POST.get('id')
        password = request.POST.get('yoneticisifre')

        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM Sifreler WHERE UserID = %s AND Password = %s", [username, password])
            user = cursor.fetchone()

            if user:
                return render(request, "admin/adminfirst.html")
            else:
                messages.error(request, 'Geçersiz kullanıcı adı veya şifre.')
                return redirect('/yonetici/giris/')

    return render(request, 'admin/adminfirst.html')

def search_appointments(request):
    search_term = request.GET.get('term')
    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT 
                R.RandevuID, 
                CONCAT(H.Ad, ' ', H.Soyad) AS HastaAdSoyad, 
                CONCAT(D.Ad, ' ', D.Soyad) AS DoktorAdSoyad, 
                R.Tarih, 
                R.Saat 
            FROM 
                Randevular R
            JOIN 
                Hastalar H ON R.HastaID = H.HastaID
            JOIN 
                Doktorlar D ON R.DoktorID = D.DoktorID
            WHERE 
                H.Ad LIKE %s OR 
                H.Soyad LIKE %s OR 
                H.HastaID LIKE %s OR 
                D.Ad LIKE %s OR 
                D.Soyad LIKE %s OR 
                D.DoktorID LIKE %s OR 
                R.Tarih LIKE %s OR 
                R.Saat LIKE %s
        """, [f'%{search_term}%', f'%{search_term}%', f'%{search_term}%', f'%{search_term}%', f'%{search_term}%', f'%{search_term}%', f'%{search_term}%', f'%{search_term}%'])
        randevular = cursor.fetchall()

    results = [{'RandevuID': randevu[0], 'HastaAdSoyad': randevu[1], 'DoktorAdSoyad': randevu[2], 'Tarih': randevu[3], 'Saat': randevu[4]} for randevu in randevular]
    return JsonResponse({'randevular': results})

def doktor_login(request):
    if request.method == 'POST':
        username = request.POST.get('id')
        password = request.POST.get('sifre')

        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM Sifreler WHERE userID = %s AND password = %s", [username, password])
            user = cursor.fetchone()

            if user:
                request.session['user_id'] = username  # Oturuma doktor ID'sini ekle
                return render(request, "doctors/doctors_main_page.html")
            else:
                messages.error(request, 'Geçersiz kullanıcı adı veya şifre.')
                return redirect('/doktor/')
    return render(request, 'doctors/doctors.html')

def doctor_ekle(request):
    with connection.cursor() as cursor:
        cursor.execute("SELECT DISTINCT UzmanlikAlani FROM Doktorlar")
        yeni_doktor = [row[0] for row in cursor.fetchall()]
    return JsonResponse({'yeni_doktor': yeni_doktor})

def search_reports(request):
    if request.method == 'GET':
        term = request.GET.get('term', '')
        with connection.cursor() as cursor:
            cursor.execute("""
                SELECT * FROM TibbiRaporlar 
                WHERE 
                    RaporID LIKE %s OR
                    RaporTarihi LIKE %s OR
                    RaporIcerigi LIKE %s OR
                    HastaID LIKE %s OR
                    DoktorID LIKE %s OR
                    YoneticiID LIKE %s
            """, [f'%{term}%', f'%{term}%', f'%{term}%', f'%{term}%', f'%{term}%', f'%{term}%'])
            results = cursor.fetchall()

        return JsonResponse({'raporlar': results})

def edit_report(request):
    if request.method == 'POST':
        rapor_id = request.POST.get('raporid')
        rapor_tarihi = request.POST.get('rapor_tarihi')
        rapor_icerigi = request.POST.get('rapor_icerigi')
        hasta_id = request.POST.get('hastaid')
        doktor_id = request.POST.get('doktorid')
        yonetici_id = request.POST.get('yoneticiid')

        rapor = TibbiRapor(rapor_id, rapor_tarihi, rapor_icerigi, hasta_id, doktor_id)
        try:
            rapor.guncelle()
            return JsonResponse({'success': True})
        except Error as e:
            return JsonResponse({'success': False, 'message': str(e)})

def admin_second_report(request):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM TibbiRaporlar")
        raporlar = cursor.fetchall()
    return render(request, 'admin/adminsecond_report.html', {'raporlar': raporlar})

def admin_second_report_post(request):
    if request.method == 'POST':
        action = request.POST.get('action')
        rapor_id = request.POST.get('raporid')
        rapor_tarihi = request.POST.get('rapor_tarihi')
        rapor_icerigi = request.POST.get('rapor_icerigi')
        hasta_id = request.POST.get('hastaid')
        doktor_id = request.POST.get('doktorid')
        yonetici_id = request.POST.get('yoneticiid')

        rapor = TibbiRapor(rapor_id, rapor_tarihi, rapor_icerigi, hasta_id, doktor_id)
        try:
            if action == 'update':
                rapor.guncelle()
                messages.success(request, 'Rapor başarıyla güncellendi.')
            elif action == 'delete':
                rapor.sil()
                messages.success(request, 'Rapor başarıyla silindi.')
            else:
                messages.error(request, 'Geçersiz işlem.')
        except Error as e:
            messages.error(request, f'Bir hata oluştu: {str(e)}')

        return redirect('admin_second_report')

def admin_second_appointment(request):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM Randevular")
        randevular = cursor.fetchall()
    return render(request, 'admin/adminsecond_appointment.html', {'randevular': randevular})

def admin_second_appointment_post(request):
    if request.method == 'POST':
        randevu_id = request.POST.get('randevuid')
        hasta_id = request.POST.get('hastaid')
        doktor_id = request.POST.get('doktorid')
        tarih = request.POST.get('tarih')
        saat = request.POST.get('saat')
        action = request.POST.get('action')

        randevu = Randevu(randevu_id, hasta_id, doktor_id, tarih, saat)
        try:
            if action == 'update':
                randevu.guncelle()
                return JsonResponse({'success': True})
            elif action == 'delete':
                randevu.sil()
                return JsonResponse({'success': True})
        except Error as e:
            return JsonResponse({'success': False, 'message': str(e)})

    return JsonResponse({'success': False, 'message': 'Invalid request method'})

def admin_search_appointments(request):
    if request.method == 'GET':
        term = request.GET.get('term', '')
        with connection.cursor() as cursor:
            cursor.execute("""
                SELECT * FROM Randevular 
                WHERE 
                    RandevuID LIKE %s OR
                    HastaID LIKE %s OR
                    DoktorID LIKE %s OR
                    Tarih LIKE %s OR
                    Saat LIKE %s
            """, [f'%{term}%', f'%{term}%', f'%{term}%', f'%{term}%', f'%{term}%'])
            results = cursor.fetchall()
        return JsonResponse({'randevular': results})

def search_patients(request):
    term = request.GET.get('term', '')
    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT * FROM Hastalar
            WHERE
                HastaID LIKE %s OR
                Ad LIKE %s OR
                Soyad LIKE %s OR
                DogumTarihi LIKE %s OR
                Cinsiyet LIKE %s OR
                TelefonNumarasi LIKE %s OR
                Adres LIKE %s
        """, [f'%{term}%', f'%{term}%', f'%{term}%', f'%{term}%', f'%{term}%', f'%{term}%', f'%{term}%'])
        hastalar = cursor.fetchall()
    return JsonResponse({'hastalar': hastalar})

def search_doctors(request):
    term = request.GET.get('term', '')
    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT * FROM doktorlar
            WHERE
                doktorid LIKE %s OR
                ad LIKE %s OR
                soyad LIKE %s OR
                uzmanlikalani LIKE %s OR
                calistigihastane LIKE %s
        """, [f'%{term}%', f'%{term}%', f'%{term}%', f'%{term}%', f'%{term}%'])
        doktorlar = cursor.fetchall()
    return JsonResponse({'doktorlar': doktorlar})

def get_doctor_appointments(request):
    doktor_id = request.session.get('user_id')  # Oturumdaki doktor ID'sini al
    if not doktor_id:
        return JsonResponse({'randevular': [], 'message': 'Doktor ID oturumda bulunamadı.'})

    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT R.RandevuID, R.DoktorID, R.HastaID, CONCAT(H.Ad, ' ', H.Soyad) AS HastaAdSoyad, R.Tarih, R.Saat
            FROM Randevular R
            JOIN Hastalar H ON R.HastaID = H.HastaID
            WHERE R.DoktorID = %s
        """, [doktor_id])
        randevular = cursor.fetchall()

    if not randevular:
        return JsonResponse({'randevular': [], 'message': 'Hiç randevu bulunamadı.'})

    # JSON response formatında dönüştür
    results = [{'RandevuID': randevu[0], 'DoktorID': randevu[1], 'HastaID': randevu[2], 'HastaAdSoyad': randevu[3], 'Tarih': randevu[4], 'Saat': randevu[5]} for randevu in randevular]
    return JsonResponse({'randevular': results, 'message': 'Randevular başarıyla bulundu.'})

def get_doctor_patients(request):
    doktor_id = request.session.get('user_id')  # Oturumdaki doktor ID'sini al
    if not doktor_id:
        return JsonResponse({'hastalar': [], 'message': 'Doktor ID oturumda bulunamadı.'})

    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT DISTINCT H.HastaID, H.Ad, H.Soyad, H.DogumTarihi, H.Cinsiyet, H.TelefonNumarasi, H.Adres
            FROM Hastalar H
            JOIN Randevular R ON H.HastaID = R.HastaID
            WHERE R.DoktorID = %s
        """, [doktor_id])
        doktor_hastalar = cursor.fetchall()

    if not doktor_hastalar:
        return JsonResponse({'hastalar': [], 'message': 'Hiç hasta bulunamadı.'})

    results = [{'HastaID': hasta[0], 'Ad': hasta[1], 'Soyad': hasta[2], 'DogumTarihi': hasta[3], 'Cinsiyet': hasta[4], 'TelefonNumarasi': hasta[5], 'Adres': hasta[6]} for hasta in doktor_hastalar]
    return JsonResponse({'hastalar': results, 'message': 'Hastalar başarıyla bulundu.'})

def get_patient_reports(request):
    doktor_id = request.session.get('user_id')  # Oturumdaki doktor ID'sini al
    if not doktor_id:
        return JsonResponse({'raporlar': [], 'message': 'Doktor ID oturumda bulunamadı.'})

    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT RaporID, RaporTarihi, RaporIcerigi, HastaID, DoktorID
            FROM TibbiRaporlar
            WHERE DoktorID = %s
        """, [doktor_id])
        raporlar = cursor.fetchall()

    if not raporlar:
        return JsonResponse({'raporlar': [], 'message': 'Hiç rapor bulunamadı.'})

    results = [{'RaporID': rapor[0], 'RaporTarihi': rapor[1], 'RaporIcerigi': rapor[2], 'HastaID': rapor[3], 'DoktorID': rapor[4]} for rapor in raporlar]
    return JsonResponse({'raporlar': results, 'message': 'Raporlar başarıyla bulundu.'})


def add_or_update_report(request):
    if request.method == 'POST':
        rapor_tarihi = request.POST.get('raporTarihi')
        rapor_icerigi = request.POST.get('raporIcerigi')
        hasta_id = request.POST.get('hastaid')
        doktor_id = request.POST.get('doktorid')
        rapor_id = request.POST.get('raporid')

        rapor = TibbiRapor(rapor_id, rapor_tarihi, rapor_icerigi, hasta_id, doktor_id)
        try:
            if rapor_id:
                rapor.guncelle()
            else:
                rapor.kaydet()

            # Bildirim ekleme
            with connection.cursor() as cursor:
                cursor.execute(
                    "INSERT INTO Bildirimler (HastaID, DoktorID, Icerik) VALUES (%s, %s, %s)",
                    [hasta_id, doktor_id, f"Yeni bir tıbbi rapor eklendi: {rapor_icerigi[:50]}..."]
                )
            connection.commit()

            return JsonResponse({'success': True, 'message': 'Rapor başarıyla kaydedildi.'})
        except Exception as e:
            return JsonResponse({'success': False, 'message': f'Bir hata oluştu: {str(e)}'})

    return JsonResponse({'success': False, 'message': 'Geçersiz istek.'})


def delete_report(request):
    if request.method == 'POST':
        rapor_id = request.POST.get('raporID')
        rapor = TibbiRapor(rapor_id, None, None, None, None)
        try:
            rapor.sil()
            return JsonResponse({'success': True, 'message': 'Rapor başarıyla silindi.'})
        except Exception as e:
            return JsonResponse({'success': False, 'message': f'Bir hata oluştu: {str(e)}'})

    return JsonResponse({'success': False, 'message': 'Geçersiz istek.'})

def delete_appointment(request):
    if request.method == 'POST':
        randevu_id = request.POST.get('randevuID')
        randevu = Randevu(randevu_id, None, None, None, None)
        try:
            randevu.sil()
            return JsonResponse({'success': True, 'message': 'Randevu başarıyla silindi.'})
        except Exception as e:
            return JsonResponse({'success': False, 'message': f'Bir hata oluştu: {str(e)}'})

    return JsonResponse({'success': False, 'message': 'Geçersiz istek.'})

def register_patient(request):
    if request.method == 'POST':
        ad = request.POST.get('ad')
        soyad = request.POST.get('soyad')
        dogum_tarihi = request.POST.get('dogum_tarihi')
        cinsiyet = request.POST.get('cinsiyet')
        telefon = request.POST.get('telefon')
        adres = request.POST.get('adres')
        sifre = request.POST.get('sifre')
        hasta_id = random.randint(100000, 999999)

        hasta = Hasta(hasta_id, ad, soyad, dogum_tarihi, cinsiyet, telefon, adres)

        try:
            hasta.kaydet()
            with connection.cursor() as cursor:
                cursor.execute("INSERT INTO Sifreler (UserID, Password) VALUES (%s, %s)", [hasta_id, sifre])
            baglanti.commit()
            return JsonResponse({'success': True, 'message': 'Hasta başarıyla kaydedildi.'})
        except Exception as e:
            return JsonResponse({'success': False, 'message': f'Bir hata oluştu: {str(e)}'})
    return JsonResponse({'success': False, 'message': 'Geçersiz istek.'})


def get_notifications(request):
    user_id = request.session.get('user_id')
    if not user_id:
        return JsonResponse({'success': False, 'message': 'Kullanıcı oturumu bulunamadı.'})

    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM Bildirimler WHERE HastaID = %s AND OkunduMu = FALSE", [user_id])
        bildirimler = cursor.fetchall()

    results = [{'BildirimID': b[0], 'HastaID': b[1], 'DoktorID': b[2], 'Icerik': b[3], 'Tarih': b[5]} for b in
               bildirimler]
    return JsonResponse({'success': True, 'bildirimler': results})


def mark_notifications_as_read(request):
    user_id = request.session.get('user_id')
    if not user_id:
        return JsonResponse({'success': False, 'message': 'Kullanıcı oturumu bulunamadı.'})

    try:
        with connection.cursor() as cursor:
            cursor.execute("UPDATE Bildirimler SET OkunduMu = TRUE WHERE HastaID = %s", [user_id])
        connection.commit()
        return JsonResponse({'success': True, 'message': 'Bildirimler okundu olarak işaretlendi.'})
    except Exception as e:
        return JsonResponse({'success': False, 'message': f'Bir hata oluştu: {str(e)}'})
