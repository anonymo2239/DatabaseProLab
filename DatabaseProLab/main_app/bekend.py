class User:
    def __init__(self, username):
        self.username = username

    def display_info(self):
        print("Username:", self.username)


class Admin(User):
    def __init__(self, username):
        super().__init__(username)

    def _add_doctor(self):
        # doktor ekleme sql, protected olarak
        pass

    def _remove_doctor(self):
        # doctor çıkartma sql, protected olarak
        pass

    def _add_report(self):
        # rapor ekleme sql, protected olarak
        pass

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
    admin = Admin("admin_user")
    doctor1 = Doctor("doctor1_user")
    doctor2 = Doctor("doctor2_user")

    admin.add_doctor(doctor1)
    admin.add_doctor(doctor2)
    admin.display_info()

    admin.remove_doctor(doctor1)
    admin.display_info()
