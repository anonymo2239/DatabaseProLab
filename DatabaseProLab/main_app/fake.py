import mysql.connector
from mysql.connector import Error
from faker import Faker
import random
from datetime import datetime

fake = Faker('tr_TR')

def create_fake_data():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="1234",
            database="prolab"
        )
        cursor = connection.cursor()

        # Yönetici ekle
        cursor.execute("""
        INSERT INTO Yonetici (YoneticiID)
        VALUES (%s)
        """, (1,))

        # Hastalar
        for _ in range(100):  # 100 hasta ekleyelim
            birthdate = fake.date_of_birth(minimum_age=18, maximum_age=73, tzinfo=None)
            while birthdate.year < 1950:
                birthdate = fake.date_of_birth(minimum_age=18, maximum_age=73, tzinfo=None)
            cursor.execute("""
            INSERT INTO Hastalar (Ad, Soyad, DogumTarihi, Cinsiyet, TelefonNumarasi, Adres)
            VALUES (%s, %s, %s, %s, %s, %s)
            """, (
                fake.first_name(),
                fake.last_name(),
                birthdate,
                random.choice(['Erkek', 'Kadın']),
                fake.numerify(text='############'),  # 12 haneli telefon numarası
                fake.address()[:150]  # Adres uzunluğunu 150 karakterle sınırla
            ))

        # Randevular
        hastalar = []
        doktorlar = []
        cursor.execute("SELECT HastaID FROM Hastalar")
        hastalar = [hasta[0] for hasta in cursor.fetchall()]
        cursor.execute("SELECT DoktorID FROM Doktorlar")
        doktorlar = [doktor[0] for doktor in cursor.fetchall()]

        for _ in range(500):  # 500 randevu ekleyelim
            randevu_tarihi = fake.date_between(start_date='today', end_date='+1y')
            randevu_saati = fake.time_object()
            hasta_id = random.choice(hastalar)
            doktor_id = random.choice(doktorlar)
            cursor.execute("""
            INSERT INTO Randevular (HastaID, DoktorID, Tarih, Saat)
            VALUES (%s, %s, %s, %s)
            """, (
                hasta_id,
                doktor_id,
                randevu_tarihi,
                randevu_saati
            ))

        connection.commit()
    except Error as e:
        print("MySQL hatası:", e)
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL bağlantısı kapatıldı")

create_fake_data()
