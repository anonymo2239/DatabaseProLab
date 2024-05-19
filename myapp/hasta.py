import mysql.connector
import random

class Hasta:
    def __init__(self, hasta_id, ad, soyad, dogum_tarihi, cinsiyet, telefon, adres):
        self.hasta_id = hasta_id
        self.ad = ad
        self.soyad = soyad
        self.dogum_tarihi = dogum_tarihi
        self.cinsiyet = cinsiyet
        self.telefon = telefon
        self.adres = adres

    def kaydet(self):
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="1234",
            database="prolab"
        )
        cursor = connection.cursor()
        cursor.execute(
            "INSERT INTO Hastalar (HastaID, Ad, Soyad, DogumTarihi, Cinsiyet, TelefonNumarasi, Adres) VALUES (%s, %s, %s, %s, %s, %s, %s)",
            [self.hasta_id, self.ad, self.soyad, self.dogum_tarihi, self.cinsiyet, self.telefon, self.adres]
        )
        connection.commit()
        cursor.close()
        connection.close()

    def guncelle(self):
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="1234",
            database="prolab"
        )
        cursor = connection.cursor()
        cursor.execute(
            "UPDATE Hastalar SET Ad=%s, Soyad=%s, DogumTarihi=%s, Cinsiyet=%s, TelefonNumarasi=%s, Adres=%s WHERE HastaID=%s",
            [self.ad, self.soyad, self.dogum_tarihi, self.cinsiyet, self.telefon, self.adres, self.hasta_id]
        )
        connection.commit()
        cursor.close()
        connection.close()

    def sil(self):
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="1234",
            database="prolab"
        )
        cursor = connection.cursor()
        cursor.execute(
            "DELETE FROM Hastalar WHERE HastaID = %s",
            [self.hasta_id]
        )
        connection.commit()
        cursor.close()
        connection.close()
