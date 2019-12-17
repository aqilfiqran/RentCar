from django.conf import settings
from django.db import models
from core.models import User
from django.utils.translation import ugettext_lazy as _
from django.utils.text import slugify
from django.urls import reverse


class Car(models.Model):
    title = models.CharField(max_length=100)
    ctipe = (
        ('Honda', 'honda'),
        ('Yamaha', 'yamaha'),
    )
    tipe = models.CharField(max_length=100, choices=ctipe)
    harga_sewa_hari = models.IntegerField(_('Price/Day'),)
    clokasi = (
        ('Banda Aceh', 'banda aceh'),
        ('Aceh Besar', 'aceh besar'),
    )
    lokasi = models.CharField(_('City'), max_length=100, choices=clokasi)
    gambar = models.ImageField(_('Image'), upload_to='car/')
    deskripsi = models.TextField(_('Description'))
    slug = models.SlugField(editable=False)
    update = models.DateTimeField(auto_now_add=True, editable=False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE, default=1)

    def save(self):
        self.slug = slugify(self.title)
        super(Car, self).save()

    def get_absolute_url(self):
        return reverse("car:detail", kwargs={"slug": self.slug})

    def __str__(self):
        return '{}. {}'.format(self.id, self.title)


class Pengecekan(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE, default=1)
    admin = models.ForeignKey(settings.AUTH_USER_MODEL,
                              on_delete=models.CASCADE, default=1)
    title = models.CharField(max_length=100)
    keterangan = models.TextField()

    def __str__(self):
        return '{}. {}'.format(self.id, self.title)


class Penyewaan(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    car = models.ForeignKey(Car, on_delete=models.CASCADE, default=1)
    tgl_sewa = models.DateTimeField(verbose_name='Start Date')
    tgl_selesai = models.DateTimeField(verbose_name='Finish Date')

    def get_absolute_url(self):
        return reverse("car:list", args=['all', 1])

    def __str__(self):
        return '{}. {} - {}'.format(self.id, self.user.name, self.car.title)
