from django.db import models

class ArticlePreparationGuide(models.Model):
    upload_file = models.FileField(upload_to='Yuriqnoma/articles/', verbose_name="Yo'riqnoma fayli")

    class Meta:
        verbose_name = 'Maqola yo\'riqnomasi'
        verbose_name_plural = 'Maqolalar yo\'riqnomasi'

    def __str__(self):
        return "Maqola Yo'riqnomasi"


class SampleDoc(models.Model):
    title_uz = models.CharField(max_length=255, verbose_name="Namunaviy hujjat nomi (UZ)")
    title_ru = models.CharField(max_length=255, verbose_name="Namunaviy hujjat nomi (RU)")
    title_en = models.CharField(max_length=255, verbose_name="Namunaviy hujjat nomi (EN)")

    content_uz = models.TextField(verbose_name='Hujjat matni (UZ)')
    content_ru = models.TextField(verbose_name='Hujjat matni (RU)')
    content_en = models.TextField(verbose_name='Hujjat matni (EN)')

    class Meta:
        verbose_name = 'Namunaviy hujjat'
        verbose_name_plural = 'Namunaviy hujjatlar'

    def __str__(self):
        return self.title_uz


class CopyRight(models.Model):
    title_uz = models.CharField(max_length=200, verbose_name="Mualliflik huquqi nomi (UZ)")
    title_ru = models.CharField(max_length=200, verbose_name="Mualliflik huquqi nomi (RU)")
    title_en = models.CharField(max_length=200, verbose_name="Mualliflik huquqi nomi (EN)")

    content_uz = models.TextField(verbose_name='Mualliflik huquqi matni (UZ)')
    content_ru = models.TextField(verbose_name='Mualliflik huquqi matni (RU)')
    content_en = models.TextField(verbose_name='Mualliflik huquqi matni (EN)')

    class Meta:
        verbose_name = 'Mualliflik huquqi'
        verbose_name_plural = 'Mualliflik huquqlari'

    def __str__(self):
        return self.title_uz
