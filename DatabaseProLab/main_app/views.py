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

def randevu_al(request):
    return render(request, "main_app/patients/randevu_al.html")

def tibbi_raporlar_duzenle(request):
    return render(request, "main_app/patients/tibbi_raporlar_duzenle.html")


# SAYFALARI SQL İLE BAĞLAMA

def hasta_kayit(request):
    if request.method == 'POST':
        # Formdan gelen verileri al
        ad = request.POST.get('ad')
        soyad = request.POST.get('soyad')
        dogum_tarihi = request.POST.get('dogum_tarihi')
        cinsiyet = request.POST.get('cinsiyet')
        telefon = request.POST.get('telefon_numarasi')
        adres = request.POST.get('adres')

        # Yeni Hasta nesnesi oluştur ve veritabanına kaydet
        yeni_hasta = Hastalar(ad=ad, soyad=soyad, dogumtarihi=dogum_tarihi, cinsiyet=cinsiyet, telefonnumarasi=telefon, adres=adres)
        yeni_hasta.save()

        # Kullanıcıya başarı mesajı göster
        messages.success(request, 'Hasta başarıyla kaydedildi.')
        return redirect('hasta_kayit')  # Başarılı kayıttan sonra sayfayı yeniden yükle
    else:
        # POST olmadığında boş formu göster
        return render(request, 'hasta_kayit.html')

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
    if request.method == 'POST':
        action = request.POST.get('action')
        
        if action == 'add':
            # Formdan bilgileri al
            hastaid = request.POST.get('hastaid')
            hasta_ad = request.POST.get('hasta_ad')
            hasta_soyad = request.POST.get('hasta_soyad')
            hasta_dogum_tarihi = request.POST.get('hasta_dogumTarihi')
            hasta_cinsiyet = request.POST.get('hasta_cinsiyet')
            hasta_telefon = request.POST.get('hasta_telefonNo')
            hasta_adres = request.POST.get('hasta_adres')

            with connection.cursor() as cursor:
                # Hastanın zaten var olup olmadığını kontrol et
                cursor.execute("SELECT * FROM hastalar WHERE hastaid = %s", [hastaid])
                row = cursor.fetchone()

                if row is None:
                    # Yeni Hasta ekle
                    cursor.execute(
                        "INSERT INTO hastalar (hastaid, ad, soyad, dogumtarihi, cinsiyet, telefonnumarasi, adres) VALUES (%s, %s, %s, %s, %s, %s, %s)",
                        [hastaid, hasta_ad, hasta_soyad, hasta_dogum_tarihi, hasta_cinsiyet, hasta_telefon, hasta_adres]
                    )
                    messages.success(request, 'Hasta başarıyla eklendi.')
                else:
                    messages.error(request, 'Bu ID ile zaten bir hasta mevcut.')

        elif action == 'update':
            # Formdan bilgileri al
            hastaid = request.POST.get('hastaid')
            hasta_ad = request.POST.get('hasta_ad')
            hasta_soyad = request.POST.get('hasta_soyad')
            hasta_dogum_tarihi = request.POST.get('hasta_dogum_tarihi')
            hasta_cinsiyet = request.POST.get('hasta_cinsiyet')
            hasta_telefon = request.POST.get('hasta_telefon')
            hasta_adres = request.POST.get('hasta_adres')

            with connection.cursor() as cursor:
                # Hastanın var olup olmadığını kontrol et
                cursor.execute("SELECT * FROM hastalar WHERE hastaid = %s", [hastaid])
                row = cursor.fetchone()

                if row is not None:
                    # Hastayı güncelle
                    cursor.execute(
                        "UPDATE hastalar SET ad = %s, soyad = %s, dogumtarihi = %s, cinsiyet = %s, telefonnumarasi = %s, adres = %s WHERE hastaid = %s",
                        [hasta_ad, hasta_soyad, hasta_dogum_tarihi, hasta_cinsiyet, hasta_telefon, hasta_adres, hastaid]
                    )
                    messages.success(request, 'Hasta başarıyla güncellendi.')
                else:
                    messages.error(request, 'Bu ID ile bir hasta bulunamadı.')

        elif action == 'delete':
            # Formdan bilgileri al
            hastaid = request.POST.get('hastaid')

            with connection.cursor() as cursor:
                # Hastanın var olup olmadığını kontrol et
                cursor.execute("SELECT * FROM hastalar WHERE hastaid = %s", [hastaid])
                row = cursor.fetchone()

                if row is not None:
                    # Hastayı sil
                    cursor.execute("DELETE FROM hastalar WHERE hastaid = %s", [hastaid])
                    messages.success(request, 'Hasta başarıyla silindi.')
                else:
                    messages.error(request, 'Bu ID ile bir hasta bulunamadı.')

        return redirect('admin_second_patient')

    else:
        # GET isteği için mevcut hastaları listele
        hastalar = Hastalar.objects.all()
        return render(request, 'main_app/admin/adminsecond_patient.html', {'hastalar': hastalar})



def admin_second_doctor(request):
    if request.method == 'POST':
        action = request.POST.get('action')
        
        if action == 'add':
            # Formdan bilgileri al
            doktorid = request.POST.get('doktorid')
            doktor_ad = request.POST.get('doktor_ad')
            doktor_soyad = request.POST.get('doktor_soyad')
            doktor_uzmanlikalani = request.POST.get('doktor_uzmanlikalani')
            doktor_calistigihastane = request.POST.get('doktor_calistigihastane')

            with connection.cursor() as cursor:
                # Doktorun zaten var olup olmadığını kontrol et
                cursor.execute("SELECT * FROM doktorlar WHERE doktorid = %s", [doktorid])
                row = cursor.fetchone()

                if row is None:
                    # Yeni Doktor ekle
                    cursor.execute(
                        "INSERT INTO doktorlar (doktorid, ad, soyad, uzmanlikalani, calistigihastane) VALUES (%s, %s, %s, %s, %s)",
                        [doktorid, doktor_ad, doktor_soyad, doktor_uzmanlikalani, doktor_calistigihastane]
                    )
                    messages.success(request, 'Doktor başarıyla eklendi.')
                else:
                    messages.error(request, 'Bu ID ile zaten bir doktor mevcut.')

        elif action == 'update':
            # Formdan bilgileri al
            doktorid = request.POST.get('doktorid')
            doktor_ad = request.POST.get('doktor_ad')
            doktor_soyad = request.POST.get('doktor_soyad')
            doktor_uzmanlikalani = request.POST.get('doktor_uzmanlikalani')
            doktor_calistigihastane = request.POST.get('doktor_calistigihastane')

            with connection.cursor() as cursor:
                # Doktorun var olup olmadığını kontrol et
                cursor.execute("SELECT * FROM doktorlar WHERE doktorid = %s", [doktorid])
                row = cursor.fetchone()

                if row is not None:
                    # Doktoru güncelle
                    cursor.execute(
                        "UPDATE doktorlar SET ad = %s, soyad = %s, uzmanlikalani = %s, calistigihastane = %s WHERE doktorid = %s",
                        [doktor_ad, doktor_soyad, doktor_uzmanlikalani, doktor_calistigihastane, doktorid]
                    )
                    messages.success(request, 'Doktor başarıyla güncellendi.')
                else:
                    messages.error(request, 'Bu ID ile bir doktor bulunamadı.')

        elif action == 'delete':
            # Formdan bilgileri al
            doktorid = request.POST.get('doktorid')

            with connection.cursor() as cursor:
                # Doktorun var olup olmadığını kontrol et
                cursor.execute("SELECT * FROM doktorlar WHERE doktorid = %s", [doktorid])
                row = cursor.fetchone()

                if row is not None:
                    # Doktoru sil
                    cursor.execute("DELETE FROM doktorlar WHERE doktorid = %s", [doktorid])
                    messages.success(request, 'Doktor başarıyla silindi.')
                else:
                    messages.error(request, 'Bu ID ile bir doktor bulunamadı.')

        elif action == 'select':
            # Formdan bilgileri al
            doktorid = request.POST.get('doktorid')

            with connection.cursor() as cursor:
                # Doktorun var olup olmadığını kontrol et
                cursor.execute("SELECT * FROM doktorlar WHERE doktorid = %s", [doktorid])
                row = cursor.fetchone()

                if row is not None:
                    messages.success(request, f'Doktor bulundu: {row}')
                else:
                    messages.error(request, 'Bu ID ile bir doktor bulunamadı.')

        return redirect('admin_second_doctor')

    # GET isteği için mevcut doktorları listele
    else:
        doktorlar = Doktorlar.objects.all()
        return render(request, 'main_app/admin/adminsecond_doctor.html', {'doktorlar': doktorlar})



def admin_second_report(request):
    return render(request, 'main_app/admin/adminsecond_report.html')

def admin_second_appointment(request):
    return render(request, 'main_app/admin/adminsecond_appointment.html')

def yonetici_login(request):
    if request.method == 'POST':
        password = request.POST.get('usersifre')

        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM Yonetici, Sifreler WHERE UserID = YoneticiID AND Password = %s", [password])
            user = cursor.fetchone()

        if user:
            return render(request, "main_app/admin/adminfirst.html")
        else:
            messages.error(request, 'Yanlış kullanıcı adı veya şifre.')
            return HttpResponseRedirect('/yonetici/giris/')

    return render(request, 'main_app/admin/adminfirst.html')


# admin hasta düzenleme bölümüne sql tablosunu aktarmak


