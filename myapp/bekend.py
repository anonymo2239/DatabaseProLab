from . import FakerSQL
import mysql.connector
from mysql.connector import Error
class User:
    def __init__(self, username):
        self.username = username

    def display_info(self):
        print("Username:", self.username)

    def _connect_to_database(self):
        try:
            connection = mysql.connector.connect(
                host='localhost',
                user='root',
                password='1234',
                database='prolab'
            )
            if connection.is_connected():
                print("Connected to database")
                return connection
        except Error as e:
            print("Error connecting to database:", e)

    def close_connection(self):
        if self.connection.is_connected():
            self.connection.close()
            print("Connection closed")


class Admin(User):
    def __init__(self, username):
        super().__init__(username)

    def add_doctor(self, ad, soyad, uzmanlik_alani, calistigi_hastane):
        try:
            cursor = self.connection.cursor()
            cursor.execute("INSERT INTO Doktorlar (Ad, Soyad, UzmanlikAlani, CalistigiHastane) VALUES (%s, %s, %s, %s)", (ad, soyad, uzmanlik_alani, calistigi_hastane))
            self.connection.commit()
            print("Doctor added successfully!")
        except Error as e:
            print("Error adding doctor:", e)

    def remove_doctor_by_id(self, doctor_id):
        try:
            cursor = self.connection.cursor()
            cursor.execute("DELETE FROM Doktorlar WHERE DoktorID = %s", (doctor_id,))
            self.connection.commit()
            print("Doctor removed successfully!")
        except Error as e:
            print("Error removing doctor:", e)

    def add_report(self, rapor_tarihi, rapor_icerigi, hasta_id, doktor_id, yonetici_id):
        try:
            cursor = self.connection.cursor()
            cursor.execute("INSERT INTO TibbiRaporlar (RaporTarihi, RaporIcerigi, HastaID, DoktorID, YoneticiID) VALUES (%s, %s, %s, %s, %s)", (rapor_tarihi, rapor_icerigi, hasta_id, doktor_id, yonetici_id))
            self.connection.commit()
            print("Report added successfully!")
        except Error as e:
            print("Error adding report:", e)

    def remove_report_by_id(self, report_id):
        try:
            cursor = self.connection.cursor()
            cursor.execute("DELETE FROM TibbiRaporlar WHERE RaporID = %s", (report_id,))
            self.connection.commit()
            print("Report removed successfully!")
        except Error as e:
            print("Error removing report:", e)

    def _remove_report(self):
        # rapor çıkartma sql, protected olarak
        pass

    def _patient_info_update(self):
        # rapor ekleme sql, protected olarak
        pass

    def _doctor_info_update(self):
        # rapor çıkartma sql, protected olarak
        pass


class Doctor(User):
    def __init__(self, username):
        super().__init__(username)

    def _add_report(self):
        # rapor ekleme sql, protected olarak
        pass

    def _remove_report(self):
        # rapor çıkartma sql, protected olarak
        pass


class Patient(User):
    def __init__(self, username):
        super().__init__(username)

    def _add_report(self):
        # rapor ekleme sql, protected olarak
        pass

    def _remove_report(self):
        # rapor çıkartma sql, protected olarak
        pass


# Kullanım Örneği
if __name__ == "__main__":
    #fake = FakerSQL

    admin = Admin("admin_user")
    doctor1 = Doctor("doctor1_user")
    doctor2 = Doctor("doctor2_user")

    admin.add_doctor(doctor1)
    admin.add_doctor(doctor2)
    admin.display_info()

    admin.remove_doctor(doctor1)
    admin.display_info()
