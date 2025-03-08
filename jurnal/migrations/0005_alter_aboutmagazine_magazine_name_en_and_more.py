# Generated by Django 5.1.6 on 2025-03-02 08:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jurnal', '0004_aboutmagazine_magazine_name_en_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aboutmagazine',
            name='magazine_name_en',
            field=models.CharField(blank=True, help_text='✅ Bu maydon avtomatik ravishda tanlanadi.', max_length=255, null=True, verbose_name='Jurnal nomi (EN)'),
        ),
        migrations.AlterField(
            model_name='aboutmagazine',
            name='magazine_name_ru',
            field=models.CharField(blank=True, help_text='✅ Bu maydon avtomatik ravishda tanlanadi.', max_length=255, null=True, verbose_name='Jurnal nomi (RU)'),
        ),
        migrations.AlterField(
            model_name='aboutmagazine',
            name='magazine_name_uz',
            field=models.CharField(blank=True, help_text='✅ Bu maydon avtomatik ravishda tanlanadi.', max_length=255, null=True, verbose_name='Jurnal nomi (UZ)'),
        ),
    ]
