from django.db import models

class Contacts(models.Model):
    image = models.ImageField(upload_to='contacts/', blank=True, null=True, verbose_name='Rasm')
    phone_numbers = models.CharField(max_length=15,
                                     blank=True, null=True, help_text="Bog'lanish uchun telefon raqami.",
                                     verbose_name='Telefon raqam')
    fax_number = models.CharField(max_length=20, blank=True, null=True, verbose_name='Faks raqam')
    email = models.EmailField(null=True, blank=True)

    address_uz = models.TextField(blank=True, null=True, verbose_name='Manzil (UZ)')
    address_ru = models.TextField(blank=True, null=True, verbose_name='Manzil (RU)')
    address_en = models.TextField(blank=True, null=True, verbose_name='Manzil (EN)')

    class Meta:
        verbose_name = 'Kontakt'
        verbose_name_plural = 'Kontaktlar'

    def __str__(self):
        return f"{self.address_uz or 'Aloqa ma’lumoti'}"

