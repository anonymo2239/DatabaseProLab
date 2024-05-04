import mysql.connector
from mysql.connector import Error
from faker import Faker
import random

fake = Faker()

def generate_rapor_icerigi():
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
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="1234",
        database="prolab"
    )

    cursor = conn.cursor()

    tables = ["TibbiRaporlar", "Randevular", "Yonetici", "Doktorlar", "Hastalar"]

    # Tabloları sil
    for table_name in tables:
        cursor.execute(f"DROP TABLE IF EXISTS {table_name}")

    # Yeni tabloları oluştur
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Hastalar (
        HastaID INT PRIMARY KEY AUTO_INCREMENT,
        Ad VARCHAR(50),
        Soyad VARCHAR(50),
        DogumTarihi DATE,
        Cinsiyet VARCHAR(10),
        TelefonNumarasi VARCHAR(20),
        Adres VARCHAR(255)
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Doktorlar (
        DoktorID INT PRIMARY KEY AUTO_INCREMENT,
        Ad VARCHAR(50),
        Soyad VARCHAR(50),
        UzmanlikAlani VARCHAR(100),
        CalistigiHastane VARCHAR(100)
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Yonetici (
        YoneticiID INT PRIMARY KEY AUTO_INCREMENT
    )
    """)

    cursor.execute("""
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

    cursor.execute("""
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
    cursor.execute("INSERT INTO Yonetici () VALUES ()")

    # Fake verileri oluştur ve ekleyin
    for _ in range(1000):
        ad = fake.first_name()
        soyad = fake.last_name()
        dogum_tarihi = fake.date_of_birth(minimum_age=18, maximum_age=100)
        cinsiyet = random.choice(["Erkek", "Kadın"])
        telefon = fake.phone_number()[:20]
        adres = fake.address()
        cursor.execute("""
        INSERT INTO Hastalar (Ad, Soyad, DogumTarihi, Cinsiyet, TelefonNumarasi, Adres) 
        VALUES (%s, %s, %s, %s, %s, %s)
        """, (ad, soyad, dogum_tarihi, cinsiyet, telefon, adres))

    for _ in range(100):
        ad = fake.first_name()
        soyad = fake.last_name()
        uzmanlik_alani = fake.job()
        hastane = fake.company()
        cursor.execute("""
        INSERT INTO Doktorlar (Ad, Soyad, UzmanlikAlani, CalistigiHastane) 
        VALUES (%s, %s, %s, %s)
        """, (ad, soyad, uzmanlik_alani, hastane))

    hastalar = list(range(1, 1001))
    doktorlar = list(range(1, 101))
    random.shuffle(hastalar)
    random.shuffle(doktorlar)
    for _ in range(600):
        hasta_id = random.randint(1, 1000)
        doktor_id = random.randint(1, 100)
        tarih = fake.date_between(start_date='-1y', end_date='today')
        saat = fake.time(pattern="%H:%M:%S", end_datetime=None)
        cursor.execute("""
        INSERT INTO Randevular (HastaID, DoktorID, Tarih, Saat) 
        VALUES (%s, %s, %s, %s)
        """, (hasta_id, doktor_id, tarih, saat))

    for _ in range(400):
        rapor_tarihi = fake.date_between(start_date='-1y', end_date='today')
        rapor_icerigi = generate_rapor_icerigi()
        hasta_id = random.randint(1, 1000)
        doktor_id = random.randint(1, 100)
        yonetici_id = 1
        cursor.execute("""
        INSERT INTO TibbiRaporlar (RaporTarihi, RaporIcerigi, HastaID, DoktorID, YoneticiID) 
        VALUES (%s, %s, %s, %s, %s)
        """, (rapor_tarihi, rapor_icerigi, hasta_id, doktor_id, yonetici_id))

    conn.commit()

except Error as e:
    print("MySQL hatası:", e)

finally:
    if conn.is_connected():
        cursor.close()
        conn.close()
        print("MySQL bağlantısı kapatıldı")
