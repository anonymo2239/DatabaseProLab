import mysql.connector

class TibbiRapor:
    def __init__(self, rapor_id, rapor_tarihi, rapor_icerigi, hasta_id, doktor_id):
        self.rapor_id = rapor_id
        self.rapor_tarihi = rapor_tarihi
        self.rapor_icerigi = rapor_icerigi
        self.hasta_id = hasta_id
        self.doktor_id = doktor_id

    def kaydet(self):
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="1234",
            database="prolab"
        )
        cursor = connection.cursor()
        cursor.execute(
            "INSERT INTO TibbiRaporlar (RaporID, RaporTarihi, RaporIcerigi, HastaID, DoktorID) VALUES (%s, %s, %s, %s, %s)",
            [self.rapor_id, self.rapor_tarihi, self.rapor_icerigi, self.hasta_id, self.doktor_id]
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
            "UPDATE TibbiRaporlar SET RaporTarihi=%s, RaporIcerigi=%s, HastaID=%s, DoktorID=%s WHERE RaporID=%s",
            [self.rapor_tarihi, self.rapor_icerigi, self.hasta_id, self.doktor_id, self.rapor_id]
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
            "DELETE FROM TibbiRaporlar WHERE RaporID = %s",
            [self.rapor_id]
        )
        connection.commit()
        cursor.close()
        connection.close()
