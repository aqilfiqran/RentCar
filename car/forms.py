from .models import Car
from django import forms


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
                    'class': 'form-control'
                }
            ),
            'deskripsi': forms.Textarea(
                attrs={
                    'class': 'form-control'
                }
            ),
        }
