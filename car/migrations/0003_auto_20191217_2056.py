# Generated by Django 2.2.8 on 2019-12-17 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car', '0002_auto_20191213_2344'),
    ]

    operations = [
        migrations.AlterField(
            model_name='penyewaan',
            name='tgl_selesai',
            field=models.DateTimeField(verbose_name='Finish Date'),
        ),
        migrations.AlterField(
            model_name='penyewaan',
            name='tgl_sewa',
            field=models.DateTimeField(verbose_name='Start Date'),
        ),
    ]