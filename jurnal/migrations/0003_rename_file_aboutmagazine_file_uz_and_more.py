# Generated by Django 5.1.6 on 2025-03-02 07:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jurnal', '0002_auto_20250302_0700'),
    ]

    operations = [
        migrations.RenameField(
            model_name='aboutmagazine',
            old_name='file',
            new_name='file_uz',
        ),
        migrations.AddField(
            model_name='aboutmagazine',
            name='file_en',
            field=models.FileField(blank=True, null=True, upload_to='jurnal_haqida_fayl/', verbose_name='Fayl (EN)'),
        ),
        migrations.AddField(
            model_name='aboutmagazine',
            name='file_ru',
            field=models.FileField(blank=True, null=True, upload_to='jurnal_haqida_fayl/', verbose_name='Fayl (RU)'),
        ),
    ]
