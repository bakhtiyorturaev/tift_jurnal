from django.db import models

class EditorialStaff(models.Model):
    content_uz = models.TextField(verbose_name="Tahririyat a'zolari ro'yxati (UZ)", null=True, blank=True)
    content_ru = models.TextField(verbose_name="Tahririyata'zolari ro'yxati (RU)", null=True, blank=True)
    content_en = models.TextField(verbose_name="Tahririyat a'zolari ro'yxati (EN)", null=True, blank=True)

    class Meta:
        verbose_name = 'Tahririyat A’zolari'
        verbose_name_plural = 'Tahririyat A’zolari'

    def __str__(self):
        return "Tahririyat A'zolari"


class HonoraryForeignEditorialMember(models.Model):
    name = models.CharField(max_length=255, verbose_name="Ism-familiyasi")
    image = models.ImageField(upload_to='tahririyat/fahriy_xorijiy_azolari/', verbose_name="Rasmi")

    position_uz = models.CharField(max_length=255, verbose_name="Lavozimi (UZ)")
    position_ru = models.CharField(max_length=255, verbose_name="Lavozimi (RU)")
    position_en = models.CharField(max_length=255, verbose_name="Lavozimi (EN)")

    class Meta:
        verbose_name = 'Fahriy Xorijiy A’zolari'
        verbose_name_plural = 'Fahriy Xorijiy A’zolari'

    def __str__(self):
        return self.name


class ForeignEditorialMember(models.Model):
    name = models.CharField(max_length=255, verbose_name="Ism-familiyasi")
    image = models.ImageField(upload_to='tahririyat/xorijiy_tahririyat_azolari/', verbose_name='Rasmi')

    position_uz = models.CharField(max_length=255, verbose_name="Lavozimi (UZ)")
    position_ru = models.CharField(max_length=255, verbose_name="Lavozimi (RU)")
    position_en = models.CharField(max_length=255, verbose_name="Lavozimi (EN)")

    university_graduated_uz = models.CharField(max_length=255, verbose_name='Ilmiy darajasi (UZ)')
    university_graduated_ru = models.CharField(max_length=255, verbose_name='Ilmiy darajasi (RU)')
    university_graduated_en = models.CharField(max_length=255, verbose_name='Ilmiy darajasi (EN)')

    class Meta:
        verbose_name = 'Xorijiy Tahririyat A’zolari'
        verbose_name_plural = 'Xorijiy Tahririyat A’zolari'

    def __str__(self):
        return self.name
