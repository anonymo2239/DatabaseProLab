import mysql.connector

class Randevu:
    def __init__(self, randevu_id, hasta_id, doktor_id, tarih, saat):
        self.randevu_id = randevu_id
        self.hasta_id = hasta_id
        self.doktor_id = doktor_id
        self.tarih = tarih
        self.saat = saat

    def kaydet(self):
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="1234",
            database="prolab"
        )
        cursor = connection.cursor()
        cursor.execute(
            "INSERT INTO Randevular (RandevuID, HastaID, DoktorID, Tarih, Saat) VALUES (%s, %s, %s, %s, %s)",
            [self.randevu_id, self.hasta_id, self.doktor_id, self.tarih, self.saat]
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
            "UPDATE Randevular SET HastaID=%s, DoktorID=%s, Tarih=%s, Saat=%s WHERE RandevuID=%s",
            [self.hasta_id, self.doktor_id, self.tarih, self.saat, self.randevu_id]
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
            "DELETE FROM Randevular WHERE RandevuID = %s",
            [self.randevu_id]
        )
        connection.commit()
        cursor.close()
        connection.close()
