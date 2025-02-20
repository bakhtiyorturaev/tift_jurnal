from django.db import models


class EditorialMember(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True, verbose_name="To'liq ism-familiyasi")
    title_1_uz = models.CharField(max_length=255, blank=True, null=True, help_text="Majburiy emas",
                                  verbose_name="Rahbariyat haqida (UZ)")
    title_1_ru = models.CharField(max_length=255, blank=True, null=True, help_text="Majburiy emas",
                                  verbose_name="Rahbariyat haqida (RU)")
    title_1_en = models.CharField(max_length=255, blank=True, null=True, help_text="Majburiy emas",
                                  verbose_name="Rahbariyat haqida (EN)")

    title_2_uz = models.CharField(max_length=255, blank=True, null=True, help_text="Majburiy emas",
                                  verbose_name="Qo'shimcha ma'lumot (UZ)")
    title_2_ru = models.CharField(max_length=255, blank=True, null=True, help_text="Majburiy emas",
                                  verbose_name="Qo'shimcha ma'lumot (RU)")
    title_2_en = models.CharField(max_length=255, blank=True, null=True, help_text="Majburiy emas",
                                  verbose_name="Qo'shimcha ma'lumot (EN)")

    image = models.ImageField(upload_to='tahririyat/tahririyat_rahbaryati/', verbose_name="Rasmi")

    class Meta:
        verbose_name = 'Tahririyat Rahbaryati'
        verbose_name_plural = 'Tahririyat Rahbaryati'

    def __str__(self):
        return self.name


class EditorialStaff(models.Model):
    content = models.TextField(verbose_name="Tahririyat a'zolari ro'yxati (UZ)")


    class Meta:
        verbose_name = 'Tahririyat A’zolari'
        verbose_name_plural = 'Tahririyat A’zolari'

    def __str__(self):
        return "Tahririyat Xodimlari"


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
