import mysql.connector
from mysql.connector import Error
from faker import Faker
from faker.providers import address, date_time, job, person, phone_number
import random
from PIL import Image, ImageDraw, ImageFont
import textwrap
import os

fake = Faker('tr_TR')
fake.add_provider(address)
fake.add_provider(date_time)
fake.add_provider(job)
fake.add_provider(person)
fake.add_provider(phone_number)

def doktor_hasteneismi_uret():
    hastaneler = [
        "Arnavutköy Devlet Hastanesi",
        "Avcılar Murat Kölük Devlet Hastanesi",
        "Başakşehir Devlet Hastanesi",
        "Bahçelievler Devlet Hastanesi",
        "Bayrampaşa Devlet Hastanesi",
        "Beşiktaş Sait Çiftçi Devlet Hastanesi",
        "Beykoz Devlet Hastanesi",
        "Büyükçekmece Mimar Sinan Devlet Hastanesi",
        "Çatalca İlyas Çokay Devlet Hastanesi",
        "Esenyurt Necmi Kadıoğlu Devlet Hastanesi",
        "Eyüpsultan Devlet Hastanesi",
        "İstinye Devlet Hastanesi",
        "Kağıthane Devlet Hastanesi",
        "Küçükçekmece Kanuni Sultan Süleyman Hastanesi",
        "Maltepe Devlet Hastanesi",
        "Pendik Devlet Hastanesi",
        "Tuzla Devlet Hastanesi",
        "Silivri Devlet Hastanesi",
        "Esenler Kadın Doğum ve Çocuk Hastalıkları Hastanesi",
        "Sultanbeyli Devlet Hastanesi",
        "Şile Devlet Hastanesi",
        "Üsküdar Devlet Hastanesi",
        "Bağcılar Eğitim ve Araştırma Hastanesi",
        "Prof. Dr. Mazhar Osman Ruh ve Sinir Hastalıkları Eğitim ve Araştırma Hastanesi, Bakırköy",
        "Bakırköy Dr. Sadi Konuk Eğitim ve Araştırma Hastanesi",
        "Metin Sabancı Baltalimanı Kemik Hastalıkları Eğitim ve Araştırma Hastanesi",
        "Erenköy Ruh ve Sinir Hastalıkları Eğitim ve Araştırma Hastanesi",
        "Fatih Sultan Mehmet Eğitim ve Araştırma Hastanesi, Ataşehir",
        "Gaziosmanpaşa Eğitim ve Araştırma Hastanesi",
        "Haseki Eğitim ve Araştırma Hastanesi",
        "Haydarpaşa Numune Eğitim ve Araştırma Hastanesi",
        "İstanbul Fizik Tedavi, Rehabilitasyon Eğitim ve Araştırma Hastanesi, Bahçelievler",
        "İstanbul Eğitim ve Araştırma Hastanesi, Cerrahpaşa",
        "Kanuni Sultan Süleyman Eğitim ve Araştırma Hastanesi, Küçükçekmece",
        "Kartal Koşuyolu Yüksek İhtisas Eğitim ve Araştırma Hastanesi",
        "Medeniyet Üniversitesi Göztepe Eğitim ve Araştırma Hastanesi",
        "Mehmet Akif Ersoy Göğüs Kalp Damar Cerrahisi Eğitim ve Araştırma Hastanesi, Küçükçekmece",
        "Dr. Siyami Ersek Göğüs Kalp ve Damar Cerrahisi Eğitim ve Araştırma Hastanesi, Haydarpaşa",
        "Süreyyapaşa Göğüs Hastalıkları ve Göğüs Cerrahisi Eğitim ve Araştırma Hastanesi, Maltepe",
        "Sarıyer Hamidiye Eftal Eğitim ve Araştırma Hastanesi",
        "Şişli Hamidiye Etfal Eğitim ve Araştırma Hastanesi",
        "Taksim Eğitim ve Araştırma Hastanesi",
        "Yakacık Doğum ve Çocuk Hastalıkları Hastanesi, Kartal",
        "Yedikule Göğüs Hastalıkları ve Göğüs Cerrahisi Eğitim ve Araştırma Hastanesi",
        "Zeynep Kamil Kadın ve Çocuk Hastalıkları Eğitim ve Araştırma Hastanesi, Üsküdar",
        "Ümraniye Eğitim ve Araştırma Hastanesi, Ümraniye",
        "Marmara Üniversitesi Pendik Eğitim ve Araştırma Hastanesi, Pendik",
        "Sancaktepe Dr. İlhan Varank Eğitim ve Araştırma Hastanesi"
    ]

    return random.choice(hastaneler)

def doktor_uzmanlik_uret():
    uzmanlik_alanlari = [
        "İç Hastalıkları",
        "Alerji Hastalıkları",
        "Endokrinoloji ve Metabolizma Hastalıkları",
        "Gastroenteroloji",
        "Nefroloji",
        "Romatoloji",
        "İş ve Meslek Hastalıkları",
        "İmmünoloji",
        "Hematoloji",
        "Geriatri",
        "Tıbbi Onkoloji",
        "Yoğun Bakım",
        "Kardiyoloji",
        "Göğüs Hastalıkları",
        "Alerjik Göğüs Hastalıkları",
        "Enfeksiyon Hastalıkları",
        "Nöroloji",
        "Psikiyatri",
        "Çocuk Sağlığı ve Hastalıkları",
        "Çocuk Kardiyolojisi",
        "Çocuk Metabolizma Hastalıkları",
        "Çocuk Endokrinolojisi",
        "Çocuk Hematolojisi",
        "Çocuk Nefrolojisi",
        "Çocuk Nörolojisi",
        "Çocuk Alerjisi",
        "Çocuk Onkolojisi",
        "Çocuk Gastroenteroloji, Hepatoloji ve Beslenme",
        "Çocuk Enfeksiyon Hastalıkları",
        "Neonatoloji",
        "Genetik",
        "Çocuk Göğüs Hastalıkları",
        "Çocuk İmmünolojisi",
        "Yoğun Bakım",
        "Çocuk Psikiyatrisi",
        "Dermatoloji",
        "Fiziksel Tıp ve Rehabilitasyon",
        "Romatoloji",
        "Genel Cerrahi",
        "Gastroentroloji Cerrahisi",
        "Çocuk Cerrahisi",
        "Çocuk Ürolojisi",
        "Göğüs Cerrahisi",
        "Kalp ve Damar Cerrahisi",
        "Çocuk Kalp ve Damar Cerrahisi",
        "Beyin ve Sinir Cerrahisi",
        "Plastik, Rekonstrüktif ve Estetik Cerrahi",
        "El Cerrahisi",
        "Ortopedi ve Travmatoloji",
        "El Cerrahisi",
        "Üroloji",
        "Çocuk Ürolojisi",
        "Androloji",
        "Kulak-Burun-Boğaz Hastalıkları",
        "Göz Hastalıkları",
        "Kadın Hastalıkları ve Doğum",
        "Üreme Endokrinolojisi ve İnfertilite",
        "Perinatoloji",
        "Anesteziyoloji ve Reanimasyon",
        "Algoloji",
        "Radyasyon Onkolojisi",
        "Radyoloji",
        "Nöroradyoloji",
        "Girişimsel Radyoloji",
        "Pediyatrik Radyoloji",
        "Nükleer Tıp",
        "Tıbbi Patoloji",
        "Sitopatoloji",
        "Dermatopatoloji",
        "Nöropatoloji",
        "Tıbbi Genetik",
        "Klinik Sitogenetik",
        "Klinik Moleküler Genetik",
        "Klinik Genetik",
        "Tıbbi Biyokimya",
        "Tıbbi Mikrobiyoloji",
        "Tıbbi Parazitoloji",
        "Viroloji",
        "İmmünoloji",
        "Mikoloji",
        "Tıbbi Farmakoloji",
        "Toksikoloji",
        "Spor Hekimliği",
        "Askeri Sahra Hekimliği",
        "Hava ve Uzay Hekimliği",
        "Sualtı Hekimliği ve Hiperbarik Tıp",
        "Acil Tıp",
        "Adli Tıp",
        "Toksikoloji",
        "Halk Sağlığı",
        "Epidemiyoloji",
        "Çevre Sağlığı",
        "İşyeri Hekimliği",
        "Okul Hekimliği",
        "Fizyoloji",
        "Aile Hekimliği",
        "Anatomi",
        "Embriyoloji ve Histoloji"
    ]
    return random.choice(uzmanlik_alanlari)

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


def text_to_image(row, folder_path):
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    # Görüntü oluştur
    image = Image.new("RGB", (800, 600), color=(255, 255, 255))
    draw = ImageDraw.Draw(image)

    # Metni görüntünün ortasına yerleştir
    try:
        font = ImageFont.truetype("arial.ttf", 24)
    except IOError:
        font = ImageFont.load_default()

    position = (50, 50)  # İlk yazının başlangıç konumu
    column_spacing = 30  # Sütunlar arası boşluk

    # Her bir sütunu alt alta yaz
    for column_name, column_value in row.items():
        if column_name != 'YoneticiID':
            text = f"{column_name}: {column_value}"
            lines = textwrap.wrap(text, width=70)  # Metni 70 karakter genişliğinde satırlara böl
            for line in lines:
                draw.text(position, line, font=font, fill="black")
                position = (position[0], position[1] + column_spacing)  # Yeni sütunun başlangıç konumu

    # Görüntüyü kaydet (RaporID ismiyle)
    image.save(os.path.join(folder_path, f"{row['RaporID']}.png"))


try:
    baglanti = mysql.connector.connect(
        host="localhost",
        user="root",
        password="1234",
        database="prolab"
    )

    if baglanti.is_connected():
        imlec = baglanti.cursor()

        tablolar = ["TibbiRaporlar", "Randevular", "Yonetici", "Doktorlar", "Hastalar", "Sifreler"]

        # Tabloları sil
        for tablo_adi in tablolar:
            imlec.execute(f"DROP TABLE IF EXISTS {tablo_adi}")

        # Yeni tabloları oluştur
        imlec.execute("""
        CREATE TABLE IF NOT EXISTS Hastalar (
            HastaID INT PRIMARY KEY,
            Ad VARCHAR(50),
            Soyad VARCHAR(50),
            DogumTarihi VARCHAR(50),
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
        CREATE TABLE IF NOT EXISTS Sifreler (
            UserID INT,
            Password VARCHAR(255)
        )
        """)

        imlec.execute("""
        CREATE TABLE IF NOT EXISTS Randevular (
            RandevuID INT PRIMARY KEY AUTO_INCREMENT,
            HastaID INT,
            DoktorID INT,
            Tarih VARCHAR(50),
            Saat VARCHAR(50),
            FOREIGN KEY (HastaID) REFERENCES Hastalar(HastaID) ON DELETE CASCADE,
            FOREIGN KEY (DoktorID) REFERENCES Doktorlar(DoktorID) ON DELETE CASCADE
        )
        """)

        imlec.execute("""
        CREATE TABLE IF NOT EXISTS TibbiRaporlar (
            RaporID INT PRIMARY KEY AUTO_INCREMENT,
            RaporTarihi VARCHAR(50),
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
        imlec.execute("""
                    INSERT INTO Sifreler (UserID, Password) 
                    VALUES (%s, %s)
                    """, (1, 1234))

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

            # Hastalar için rastgele şifre oluştur ve ekleyin
            imlec.execute("""
            INSERT INTO Sifreler (UserID, Password) 
            VALUES (%s, %s)
            """, (hasta_id, fake.password(6)))

        for _ in range(100):
            # Benzersiz bir DoktorID üret
            doktor_id = fake.random_number(digits=5, fix_len=True)
            while doktor_id in doktorlar_id:  # Eğer daha önce kullanıldıysa, tekrar üret
                doktor_id = fake.random_number(digits=5, fix_len=True)
            doktorlar_id.add(doktor_id)

            ad = fake.first_name()
            soyad = fake.last_name()
            uzmanlik_alani = doktor_uzmanlik_uret()
            hastane = doktor_hasteneismi_uret()
            imlec.execute("""
            INSERT INTO Doktorlar (DoktorID, Ad, Soyad, UzmanlikAlani, CalistigiHastane) 
            VALUES (%s, %s, %s, %s, %s)
            """, (doktor_id, ad, soyad, uzmanlik_alani, hastane))

            # Doktorlar için rastgele şifre oluştur ve ekleyin
            imlec.execute("""
            INSERT INTO Sifreler (UserID, Password) 
            VALUES (%s, %s)
            """, (doktor_id, fake.password(6)))

        for _ in range(600):
            hasta_id = random.choice(list(hastalar_id))
            doktor_id = random.choice(list(doktorlar_id))
            # Rastgele bir tarih ve saat oluştur
            randevu_tarihi = fake.date_between(start_date='today', end_date='+1y')
            randevu_saati = fake.time_object()
            # Tarih ve saat uygun formata dönüştürülüyor
            randevu_tarihi_str = randevu_tarihi.strftime("%Y-%m-%d")
            randevu_saati_str = randevu_saati.strftime("%H:%M:%S")
            # Randevuyu ekleyin
            imlec.execute("""
            INSERT INTO Randevular (HastaID, DoktorID, Tarih, Saat) 
            VALUES (%s, %s, %s, %s)
            """, (hasta_id, doktor_id, randevu_tarihi_str, randevu_saati_str))

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

        cursor = baglanti.cursor(dictionary=True)
        cursor.execute("SELECT * FROM TibbiRaporlar")

        rows = cursor.fetchall()
        for row in rows:
            text_to_image(row, "TibbiRaporlar")

except Error as e:
    print("MySQL hatası:", e)

finally:
    if baglanti and baglanti.is_connected():
        imlec.close()
        baglanti.close()
        print("MySQL bağlantısı kapatıldı")
