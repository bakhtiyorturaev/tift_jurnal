from django.db import models
from django_ckeditor_5.fields import CKEditor5Field

class ArticlePreparationGuide(models.Model):
    upload_file = models.FileField(upload_to='Yuriqnoma/articles/', verbose_name="Yo'riqnoma fayli")

    class Meta:
        verbose_name = 'Maqola yo\'riqnomasi'
        verbose_name_plural = 'Maqolalar yo\'riqnomasi'

    def __str__(self):
        return "Maqola Yo'riqnomasi"

class SampleDoc(models.Model):
    title = models.CharField(max_length=255, verbose_name="namunaviy hujjat nomi")
    content = CKEditor5Field(config_name='extends')

    class Meta:
        verbose_name = 'Namunaviy hujjat'
        verbose_name_plural = 'Namunaviy hujjatlari'

    def __str__(self):
        return self.title

class CopyRight(models.Model):
    title = models.CharField(max_length=200, verbose_name="Mualliflik huquqi nomi")
    content = CKEditor5Field(config_name='extends')

    class Meta:
        verbose_name = 'Mualliflik huquqi'
        verbose_name_plural = 'Mualliflik huquqlari'

    def __str__(self):
        return self.title

