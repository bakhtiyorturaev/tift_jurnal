from django.db import models
from django_ckeditor_5.fields import CKEditor5Field

class EditorialMember(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True, verbose_name="To'liq ism-familiyasi")
    title_1 = models.CharField(max_length=255, blank=True, null=True, help_text="Majburiy emas", verbose_name="rahbariyat haqida")
    title_2 = models.CharField(max_length=255, blank=True, null=True, help_text="Majnuriy emas", verbose_name="rahbariyat haqida")
    image = models.ImageField(upload_to='tahririyat/tahririyat_rahbaryati/', verbose_name="rasmi")

    class Meta:
        verbose_name = 'Tahririyat Rahbaryati'
        verbose_name_plural = 'Tahririyat Rahbaryati'

    def __str__(self):
        return self.name

class EditorialStaff(models.Model):
    content = CKEditor5Field(config_name='extends', verbose_name="Tahririyat a'zolari ro'yxati")

    class Meta:
        verbose_name = 'Tahririyat Azolari'
        verbose_name_plural = 'Tahririyat Azolari'

    def __str__(self):
        return "Tahririyat Xodimlar"

class HonoraryForeignEditorialMember(models.Model):
    name = models.CharField(max_length=255, verbose_name="Ism-familiyasi")
    image = models.ImageField(upload_to='tahririyat/fahriy_xorijiy_azolari/', verbose_name="rasmi")
    position = models.CharField(max_length=255, verbose_name="lavozimi")

    class Meta:
        verbose_name = 'Fahriy Xorijiy Azolari'
        verbose_name_plural = 'Fahriy Xorijiy Azolari'

    def __str__(self):
        return self.name

class ForeignEditorialMember(models.Model):
    name = models.CharField(max_length=255, verbose_name="Ism-familiyasi")
    image = models.ImageField(upload_to='tahririyat/xorijiy_tahririyat_azolari/', verbose_name='rasmi')
    position = models.CharField(max_length=255, verbose_name="lvozimi")
    university_graduated = models.CharField(max_length=255, verbose_name='ilmiy darajasi')

    class Meta:
        verbose_name = 'Xorijiy Tahririyat Azolari'
        verbose_name_plural = 'Xorijiy Tahririyat Azolari'

    def __str__(self):
        return self.name
