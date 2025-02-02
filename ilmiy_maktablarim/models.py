from django.db import models


class IlmiyMaktablarim(models.Model):
    name = models.CharField(max_length=200,blank=True, null=True, verbose_name="To'liq ism familiya")
    academic_degree = models.CharField(max_length=200, blank=True, null=True,
                                       help_text="Masalan: Iqtisodiyot fanlari doktori, akademik", verbose_name="ilmiy daraja")
    haqida = models.TextField(blank=True, null=True, verbose_name="haqida")

    class Meta:
        verbose_name = 'Ilmiy maktab'
        verbose_name_plural = 'Ilmiy maktablarim'

    def __str__(self):
        return self.name

