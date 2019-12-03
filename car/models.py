from django.db import models

# Create your models here.


class Car(models.Model):
    title = models.CharField(max_length=100)
    tipe = models.CharField(max_length=100)
    harga_sewa_hari = models.IntegerField()
    lokasi = models.CharField(max_length=100)
    gambar = models.ImageField()
    deskripsi = models.TextField()

    def __str__(self):
        return self.title
