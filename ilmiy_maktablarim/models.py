from django.db import models
from django.utils.text import slugify
from django_ckeditor_5.fields import CKEditor5Field


class IlmiyMaktablarim(models.Model):
    name = models.CharField(max_length=200,blank=True, null=True, verbose_name="To'liq ism familiya")
    image = models.ImageField(upload_to='ilmiy_maktablarimiz/', blank=True, null=True, verbose_name="rasm")
    academic_degree = models.CharField(max_length=200, blank=True, null=True,
                                       help_text="Masalan: Iqtisodiyot fanlari doktori, akademik", verbose_name="ilmiy daraja")
    bio = CKEditor5Field(config_name='extends', blank=True, null=True, verbose_name="haqida")
    slug = models.SlugField(max_length=200, unique=True, blank=True)

    class Meta:
        verbose_name = 'Ilmiy maktab'
        verbose_name_plural = 'Ilmiy maktablarim'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

