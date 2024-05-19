import mysql.connector

class Doktor:
    def __init__(self, doktor_id, ad, soyad, uzmanlik_alani, calistigi_hastane):
        self.doktor_id = doktor_id
        self.ad = ad
        self.soyad = soyad
        self.uzmanlik_alani = uzmanlik_alani
        self.calistigi_hastane = calistigi_hastane

    def kaydet(self):
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="1234",
            database="prolab"
        )
        cursor = connection.cursor()
        cursor.execute(
            "INSERT INTO Doktorlar (DoktorID, Ad, Soyad, UzmanlikAlani, CalistigiHastane) VALUES (%s, %s, %s, %s, %s)",
            [self.doktor_id, self.ad, self.soyad, self.uzmanlik_alani, self.calistigi_hastane]
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
            "UPDATE Doktorlar SET Ad=%s, Soyad=%s, UzmanlikAlani=%s, CalistigiHastane=%s WHERE DoktorID=%s",
            [self.ad, self.soyad, self.uzmanlik_alani, self.calistigi_hastane, self.doktor_id]
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
            "DELETE FROM Doktorlar WHERE DoktorID = %s",
            [self.doktor_id]
        )
        connection.commit()
        cursor.close()
        connection.close()
