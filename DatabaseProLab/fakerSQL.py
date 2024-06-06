import random
from faker import Faker
from faker.providers import address, date_time, job, person, phone_number
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
        # ... (diğer hastane isimleri)
        "Sancaktepe Dr. İlhan Varank Eğitim ve Araştırma Hastanesi"
    ]
    return random.choice(hastaneler)

def doktor_uzmanlik_uret():
    uzmanlik_alanlari = [
        "İç Hastalıkları",
        "Alerji Hastalıkları",
        # ... (diğer uzmanlık alanları)
        "Embriyoloji ve Histoloji"
    ]
    return random.choice(uzmanlik_alanlari)

def rapor_icerigi_uret():
    raporlar = [
        "Hasta, grip belirtileri göstermektedir: ateş, öksürük, boğaz ağrısı.",
        "Doktor, hastanın solunum hızını değerlendirdi ve normal sınırlarda olduğunu belirledi.",
        # ... (diğer rapor içerikleri)
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

# Sahte verileri oluştur ve resimlere kaydet
folder_path = "C:\\Users\\Alperen Arda\\OneDrive\\Desktop\\GitHub\\DatabaseProLab\\DatabaseProLab\\static\\images\\reports"

for i in range(600):
    row = {
        'RaporID': i + 1,
        'RaporTarihi': fake.date_between(start_date='-1y', end_date='today').strftime('%Y-%m-%d'),
        'RaporIcerigi': rapor_icerigi_uret(),
        'HastaID': fake.random_number(digits=5, fix_len=True),
        'DoktorID': fake.random_number(digits=5, fix_len=True),
        'YoneticiID': 1
    }
    text_to_image(row, folder_path)

print("Sahte raporlar oluşturuldu ve resimler kaydedildi.")
