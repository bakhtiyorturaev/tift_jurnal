from django.db import models
from bosh_sahifa.models import Magazine


class AboutMagazine(models.Model):
    magazine = models.ForeignKey(to=Magazine, on_delete=models.CASCADE, verbose_name="Jurnal", null=True, blank=True)

    name_uz = models.CharField(max_length=255, verbose_name="Jurnal nomi (UZ)", blank=True, null=True,
                                        help_text="✅ Bu maydon avtomatik ravishda tanlanadi.")
    name_ru = models.CharField(max_length=255, verbose_name="Jurnal nomi (RU)", blank=True, null=True,
                                        help_text="✅ Bu maydon avtomatik ravishda tanlanadi.")
    name_en = models.CharField(max_length=255, verbose_name="Jurnal nomi (EN)", blank=True, null=True,
                                        help_text="✅ Bu maydon avtomatik ravishda tanlanadi.")

    bio_uz = models.TextField(verbose_name="Jurnal haqida (UZ)", blank=True, null=True)
    bio_ru = models.TextField(verbose_name="Jurnal haqida (RU)", blank=True, null=True)
    bio_en = models.TextField(verbose_name="Jurnal haqida (EN)", blank=True, null=True)

    file_uz = models.FileField(upload_to='jurnal_haqida_fayl/', verbose_name="Fayl (UZ)", blank=True, null=True)
    file_ru = models.FileField(upload_to='jurnal_haqida_fayl/', verbose_name="Fayl (RU)", blank=True, null=True)
    file_en = models.FileField(upload_to='jurnal_haqida_fayl/', verbose_name="Fayl (EN)", blank=True, null=True)

    class Meta:
        verbose_name = "Jurnal haqida"
        verbose_name_plural = "Jurnal haqida"

    def save(self, *args, **kwargs):
        if self.magazine:
            self.name_uz = self.magazine.name_uz
            self.name_ru = self.magazine.name_ru
            self.name_en = self.magazine.name_en
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.name_uz or 'Noma\'lum jurnal'} - haqida"


class MagazineNews(models.Model):
    magazine = models.ForeignKey(to=Magazine, on_delete=models.CASCADE, verbose_name="Jurnal nomi")
    title_uz = models.CharField(max_length=500, verbose_name="Yangilik nomi (UZ)", blank=True, null=True)
    title_ru = models.CharField(max_length=500, verbose_name="Yangilik nomi (RU)", blank=True, null=True)
    title_en = models.CharField(max_length=500, verbose_name="Yangilik nomi (EN)", blank=True, null=True)

    content_uz = models.TextField(verbose_name="Yangilik haqida (UZ)", blank=True, null=True)
    content_ru = models.TextField(verbose_name="Yangilik haqida (RU)", blank=True, null=True)
    content_en = models.TextField(verbose_name="Yangilik haqida (EN)", blank=True, null=True)
    news_file = models.FileField(upload_to='jurnal/news', help_text="Agar yangilik haqida fayl mavjud bo'lsa",
                                 blank=True, null=True)

    news_image = models.ImageField(upload_to='jurnal/news', blank=True, null=True, verbose_name="Rasm")
    link = models.URLField(blank=True, null=True, verbose_name="Havola",
                           help_text="Agar yangilik haqida havola mavjud bo'lsa")

    class Meta:
        verbose_name = "Yangilik"
        verbose_name_plural = "Jurnal yangiliklari"

    def __str__(self):
        return f"{self.title_uz} - {self.magazine.name_uz}"

class MagazineRequirements(models.Model):
    title_uz = models.CharField(max_length=200, verbose_name="Jurnal talablari nomi (UZ)")
    title_ru = models.CharField(max_length=200, verbose_name="Jurnal talablari nomi (RU)", blank=True, null=True)
    title_en = models.CharField(max_length=200, verbose_name="Jurnal talablari nomi (EN)", blank=True, null=True)

    content_uz = models.TextField(verbose_name="Jurnal talablari to'liq (UZ)", blank=True, null=True)
    content_ru = models.TextField(verbose_name="Jurnal talablari to'liq (RU)", blank=True, null=True)
    content_en = models.TextField(verbose_name="Jurnal talablari to'liq (EN)", blank=True, null=True)

    class Meta:
        verbose_name = "Jurnal talablari"
        verbose_name_plural = "Jurnal talablari"

    def __str__(self):
        return self.title_uz


class Statistics(models.Model):
    magazine = models.OneToOneField(Magazine, on_delete=models.CASCADE, blank=True, null=True,
                                    related_name='statistics', verbose_name="Jurnal")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Statistika kiritilgan sana")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Statistika yangilangan sana")

    def magazine_info(self):
        """Jurnal haqida to‘liq ma'lumot: sana va nechanchi sonligi"""
        return f"{self.magazine.created_at.year}-yil, {self.magazine.which_number}, {self.magazine.created_at.strftime('%B')}"

    def articles_count(self):
        """O‘sha jurnalga tegishli maqolalar soni"""
        return self.magazine.articles.count()

    class Meta:
        verbose_name = "Statistika"
        verbose_name_plural = "Statistikalar"

    def __str__(self):
        return f"Statistika: {self.magazine.name_uz}"
