from .models import Car, Penyewaan
from django import forms


class PenyewaanForm(forms.ModelForm):
    class Meta:
        model = Penyewaan
        fields = ['tgl_sewa', 'tgl_selesai']
        widgets = {
            'tgl_sewa': forms.DateTimeInput(
                attrs={
                    'class': 'form-control datetimepicker'
                }
            ),
            'tgl_selesai': forms.DateTimeInput(
                attrs={
                    'class': 'form-control datetimepicker'
                }
            ),
        }


class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ['title', 'tipe', 'harga_sewa_hari',
                  'lokasi', 'gambar', 'deskripsi']
        widgets = {
            'title': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Your Title'
                }
            ),
            'tipe': forms.Select(
                attrs={
                    'class': 'form-control',
                }
            ),
            'harga_sewa_hari': forms.TextInput(
                attrs={
                    'class': 'form-control',
                }
            ),
            'lokasi': forms.Select(
                attrs={
                    'class': 'form-control',
                }
            ),
            'gambar': forms.FileInput(
                attrs={
                    # 'accept': '.jpg,.png,.jpeg',
                    'class': 'form-control',
                }
            ),
            'deskripsi': forms.Textarea(
                attrs={
                    'class': 'form-control'
                }
            ),
        }
