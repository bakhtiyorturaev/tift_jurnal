from django.db import models

class IlmiyMaktablarim(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True, verbose_name="To'liq ism familiya")

    # Har bir til uchun ilmiy daraja
    academic_degree_uz = models.CharField(
        max_length=200, blank=True, null=True,
        help_text="Masalan: Iqtisodiyot fanlari doktori, akademik",
        verbose_name="Ilmiy daraja (UZ)"
    )
    academic_degree_ru = models.CharField(
        max_length=200, blank=True, null=True,
        help_text="Например: Доктор экономических наук, академик",
        verbose_name="Ilmiy daraja (RU)"
    )
    academic_degree_en = models.CharField(
        max_length=200, blank=True, null=True,
        help_text="For example: Doctor of Economic Sciences, academician",
        verbose_name="Ilmiy daraja (EN)"
    )

    haqida_uz = models.TextField(blank=True, null=True, verbose_name="Haqida (UZ)")
    haqida_ru = models.TextField(blank=True, null=True, verbose_name="Haqida (RU)")
    haqida_en = models.TextField(blank=True, null=True, verbose_name="Haqida (EN)")

    class Meta:
        verbose_name = 'Ilmiy maktab'
        verbose_name_plural = 'Ilmiy maktablarim'

    def __str__(self):
        return self.name
