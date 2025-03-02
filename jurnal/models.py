from django.db import models
from bosh_sahifa.models import Magazine


class AboutMagazine(models.Model):
    magazine = models.ForeignKey(
        to=Magazine,
        on_delete=models.CASCADE,
        verbose_name="Jurnal nomi",
        blank=True,
        null=True
    )

    bio_uz = models.TextField(verbose_name="Jurnal haqida (UZ)", null=True, blank=True)
    bio_ru = models.TextField(verbose_name="Jurnal haqida (RU)", blank=True, null=True)
    bio_en = models.TextField(verbose_name="Jurnal haqida (EN)", blank=True, null=True)
    file = models.FileField(upload_to='jurnal_haqida_fayl/', verbose_name="fayl", blank=True, null=True)

    class Meta:
        verbose_name = "Jurnal haqida"
        verbose_name_plural = "Jurnal haqida"

    def __str__(self):
        return f"{self.magazine.name_uz} | {self.magazine.name_ru} | {self.magazine.name_en} - haqida"

    @property
    def magazine_name_uz(self):
        return self.magazine.name_uz if self.magazine else "Noma'lum jurnal"

    @property
    def magazine_name_ru(self):
        return self.magazine.name_ru if self.magazine else "Неизвестный журнал"

    @property
    def magazine_name_en(self):
        return self.magazine.name_en if self.magazine else "Unknown Journal"



class MagazineNews(models.Model):
    magazine = models.ForeignKey(to=Magazine, on_delete=models.CASCADE, verbose_name="Jurnal nomi")
    title_uz = models.CharField(max_length=500, verbose_name="Yangilik nomi (UZ)")
    title_ru = models.CharField(max_length=500, verbose_name="Yangilik nomi (RU)", blank=True, null=True)
    title_en = models.CharField(max_length=500, verbose_name="Yangilik nomi (EN)", blank=True, null=True)

    content_uz = models.TextField(verbose_name="Yangilik haqida (UZ)")
    content_ru = models.TextField(verbose_name="Yangilik haqida (RU)", blank=True, null=True)
    content_en = models.TextField(verbose_name="Yangilik haqida (EN)", blank=True, null=True)

    image = models.ImageField(upload_to='jurnal/news', blank=True, null=True, verbose_name="Rasm")
    link = models.URLField(blank=True, null=True, verbose_name="Havola")

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
    magazine = models.OneToOneField(Magazine, on_delete=models.CASCADE, blank=True, null=True, related_name='statistics', verbose_name="Jurnal")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Statistika kiritilgan sana")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Statistika yangilangan sana")

    def magazine_info(self):
        """Jurnal haqida to‘liq ma'lumot: sana va nechanchi sonligi"""
        return f"{self.magazine.created_at.year}-yil, {self.magazine.which_number}-son, {self.magazine.created_at.strftime('%B')}"

    def articles_count(self):
        """O‘sha jurnalga tegishli maqolalar soni"""
        return self.magazine.articles.count()

    class Meta:
        verbose_name = "Statistika"
        verbose_name_plural = "Statistikalar"

    def __str__(self):
        return f"Statistika: {self.magazine.name_uz}"
