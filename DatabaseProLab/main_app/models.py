from django.db import models

# Create your models here.

class Doktorlar(models.Model):
    doktorID = models.IntegerField(primary_key=True)
    doktor_ad = models.CharField(max_length=50)
    doktor_soyad = models.CharField(max_length=50)
    doktor_uzmanlikAlani = models.CharField(max_length=50)
    doktor_calistigiHastane = models.CharField(max_length=50)

class Hastalar(models.Model):
    hastaID = models.IntegerField(primary_key=True)
    hasta_ad = models.CharField(max_length=50)
    hasta_soyad = models.CharField(max_length=50)
    hasta_dogumTarihi = models.DateTimeField()
    hasta_cinsiyet = models.CharField(max_length=6)
    hasta_telefonNo = models.CharField(max_length=14)
    hasta_adres = models.CharField(max_length=200)

class