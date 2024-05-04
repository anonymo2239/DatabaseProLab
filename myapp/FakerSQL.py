import mysql.connector
from mysql.connector import Error
from faker import Faker
from faker.providers import address, date_time, job, person, phone_number
import random

fake = Faker('tr_TR')
fake.add_provider(address)
fake.add_provider(date_time)
fake.add_provider(job)
fake.add_provider(person)
fake.add_provider(phone_number)

def rapor_icerigi_uret():
    raporlar = [
        "Hasta, grip belirtileri göstermektedir: ateş, öksürük, boğaz ağrısı.",
        "Doktor, hastanın solunum hızını değerlendirdi ve normal sınırlarda olduğunu belirledi.",
        "Hastanın kan basıncı ölçüldü ve yüksek olduğu tespit edildi.",
        "Doktor, hastanın genel durumunu değerlendirdi ve semptomların bir viral enfeksiyona işaret ettiğini düşündü.",
        "Hastanın kan testleri yapıldı ve beyaz kan hücrelerinde artış olduğu görüldü.",
        "Hasta, antibiyotik tedavisi ve istirahat önerileri ile taburcu edildi.",
        "Doktor, hastanın ateşini ölçtü ve yüksek olduğunu belirledi.",
        "Hastanın solunum sistemi incelendi ve enfeksiyon belirtileri tespit edildi.",
        "Doktor, hastanın kan değerlerini inceledi ve düşük demir seviyeleri tespit edildi.",
        "Hasta, bulantı ve baş dönmesi şikayetleriyle başvurdu.",
        "Doktor, hastanın nabzını kontrol etti ve normal olduğunu belirledi.",
        "Hastanın göğüs röntgeni çekildi ve akciğerlerinde iltihaplanma tespit edildi.",
        "Doktor, hastanın cilt muayenesini gerçekleştirdi ve döküntülerin varlığını belirledi.",
        "Hasta, karın ağrısı ve ishal şikayetleriyle geldi.",
        "Doktor, hastanın karın bölgesini muayene etti ve hassasiyet olduğunu tespit etti.",
        "Hastanın idrar testi yapıldı ve idrarında enfeksiyon belirtileri görüldü.",
        "Doktor, hastanın baş ağrısını değerlendirdi ve migren tanısı koydu.",
        "Hasta, yorgunluk ve halsizlik şikayetleriyle muayene oldu.",
        "Doktor, hastanın kan şekerini ölçtü ve yüksek olduğunu belirledi.",
        "Hastanın göz muayenesi yapıldı ve görme bozuklukları tespit edildi.",
        "Doktor, hastanın eklemlerini muayene etti ve iltihaplanma belirtileri görüldü.",
        "Hastanın kanında yüksek kolesterol seviyeleri tespit edildi.",
        "Doktor, hastanın aile öyküsünü inceledi ve genetik hastalık risklerini değerlendirdi.",
        "Hasta, kuru öksürük ve nefes darlığı şikayetleriyle geldi.",
        "Doktor, hastanın akciğer fonksiyon testlerini değerlendirdi ve astım tanısı koydu.",
        "Hastanın deri biyopsisi yapıldı ve cilt kanseri belirtileri tespit edildi.",
        "Doktor, hastanın boyun bölgesinde lenf bezlerini kontrol etti ve şişkinlik olduğunu belirledi.",
        "Hastanın kanında düşük trombosit seviyeleri tespit edildi.",
        "Doktor, hastanın mide rahatsızlıklarını inceledi ve reflü tanısı koydu.",
        "Hastanın kas ağrıları ve eklem sertlikleri şikayetleriyle başvurdu.",
        "Doktor, hastanın kas güçsüzlüğünü değerlendirdi ve romatoid artrit belirtileri görüldü."
    ]
    return random.choice(raporlar)

try:
    baglanti = mysql.connector.connect(
        host="localhost",
        user="root",
        password="1234",
        database="prolab"
    )

    imlec = baglanti.cursor()

    tablolar = ["TibbiRaporlar", "Randevular", "Yonetici", "Doktorlar", "Hastalar"]

    # Tabloları sil
    for tablo_adi in tablolar:
        imlec.execute(f"DROP TABLE IF EXISTS {tablo_adi}")

    # Yeni tabloları oluştur
    imlec.execute("""
    CREATE TABLE IF NOT EXISTS Hastalar (
        HastaID INT PRIMARY KEY,
        Ad VARCHAR(50),
        Soyad VARCHAR(50),
        DogumTarihi DATE,
        Cinsiyet VARCHAR(10),
        TelefonNumarasi VARCHAR(20),
        Adres VARCHAR(255)
    )
    """)

    imlec.execute("""
    CREATE TABLE IF NOT EXISTS Doktorlar (
        DoktorID INT PRIMARY KEY,
        Ad VARCHAR(50),
        Soyad VARCHAR(50),
        UzmanlikAlani VARCHAR(100),
        CalistigiHastane VARCHAR(100)
    )
    """)

    imlec.execute("""
    CREATE TABLE IF NOT EXISTS Yonetici (
        YoneticiID INT PRIMARY KEY
    )
    """)

    imlec.execute("""
    CREATE TABLE IF NOT EXISTS Randevular (
        RandevuID INT PRIMARY KEY AUTO_INCREMENT,
        HastaID INT,
        DoktorID INT,
        Tarih DATE,
        Saat TIME,
        FOREIGN KEY (HastaID) REFERENCES Hastalar(HastaID) ON DELETE CASCADE,
        FOREIGN KEY (DoktorID) REFERENCES Doktorlar(DoktorID) ON DELETE CASCADE
    )
    """)

    imlec.execute("""
    CREATE TABLE IF NOT EXISTS TibbiRaporlar (
        RaporID INT PRIMARY KEY AUTO_INCREMENT,
        RaporTarihi DATE,
        RaporIcerigi TEXT,
        HastaID INT,
        DoktorID INT,
        YoneticiID INT,
        FOREIGN KEY (HastaID) REFERENCES Hastalar(HastaID) ON DELETE CASCADE,
        FOREIGN KEY (DoktorID) REFERENCES Doktorlar(DoktorID) ON DELETE CASCADE,
        FOREIGN KEY (YoneticiID) REFERENCES Yonetici(YoneticiID) ON DELETE CASCADE
    )
    """)

    # Yönetici tablosuna bir giriş ekle
    imlec.execute("INSERT INTO Yonetici (YoneticiID) VALUES (1)")

    # Sahte verileri oluştur ve ekleyin
    hastalar_id = set()  # Tüm hastaların ID'lerini saklayacak küme
    doktorlar_id = set()  # Tüm doktorların ID'lerini saklayacak küme

    for _ in range(1000):
        # Benzersiz bir HastaID üret
        hasta_id = fake.random_number(digits=5, fix_len=True)
        while hasta_id in hastalar_id:  # Eğer daha önce kullanıldıysa, tekrar üret
            hasta_id = fake.random_number(digits=5, fix_len=True)
        hastalar_id.add(hasta_id)

        ad = fake.first_name()
        soyad = fake.last_name()
        dogum_tarihi = fake.date_of_birth(minimum_age=18, maximum_age=100)
        cinsiyet = random.choice(["Erkek", "Kadın"])
        telefon = fake.phone_number()[:20]
        adres = fake.address()
        imlec.execute("""
        INSERT INTO Hastalar (HastaID, Ad, Soyad, DogumTarihi, Cinsiyet, TelefonNumarasi, Adres) 
        VALUES (%s, %s, %s, %s, %s, %s, %s)
        """, (hasta_id, ad, soyad, dogum_tarihi, cinsiyet, telefon, adres))

    for _ in range(100):
        # Benzersiz bir DoktorID üret
        doktor_id = fake.random_number(digits=5, fix_len=True)
        while doktor_id in doktorlar_id:  # Eğer daha önce kullanıldıysa, tekrar üret
            doktor_id = fake.random_number(digits=5, fix_len=True)
        doktorlar_id.add(doktor_id)

        ad = fake.first_name()
        soyad = fake.last_name()
        uzmanlik_alani = fake.job()
        hastane = fake.company()
        imlec.execute("""
        INSERT INTO Doktorlar (DoktorID, Ad, Soyad, UzmanlikAlani, CalistigiHastane) 
        VALUES (%s, %s, %s, %s, %s)
        """, (doktor_id, ad, soyad, uzmanlik_alani, hastane))

    for _ in range(600):
        hasta_id = random.choice(list(hastalar_id))
        doktor_id = random.choice(list(doktorlar_id))
        tarih = fake.date_between(start_date='-1y', end_date='today')
        saat = fake.time(pattern="%H:%M:%S", end_datetime=None)
        imlec.execute("""
        INSERT INTO Randevular (HastaID, DoktorID, Tarih, Saat) 
        VALUES (%s, %s, %s, %s)
        """, (hasta_id, doktor_id, tarih, saat))

    for _ in range(400):
        rapor_tarihi = fake.date_between(start_date='-1y', end_date='today')
        rapor_icerigi = rapor_icerigi_uret()
        hasta_id = random.choice(list(hastalar_id))
        doktor_id = random.choice(list(doktorlar_id))
        yonetici_id = 1
        imlec.execute("""
        INSERT INTO TibbiRaporlar (RaporTarihi, RaporIcerigi, HastaID, DoktorID, YoneticiID) 
        VALUES (%s, %s, %s, %s, %s)
        """, (rapor_tarihi, rapor_icerigi, hasta_id, doktor_id, yonetici_id))

    baglanti.commit()

except Error as e:
    print("MySQL hatası:", e)

finally:
    if baglanti.is_connected():
        imlec.close()
        baglanti.close()
        print("MySQL bağlantısı kapatıldı")
