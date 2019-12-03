from django.db import models
from django.contrib.auth.models import User
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


class Pengecekan(models.Model):
    car_id = models.ForeignKey(Car, on_delete=models.CASCADE)
    admin_id = models.ForeignKey(User, on_delete=models.CASCADE)
    keterangan = models.TextField()
    slug = models.SlugField()

    def __str__(self):
        return self.slug
