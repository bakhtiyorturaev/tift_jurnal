from django.db import models
from django.utils.text import slugify

class Magazine(models.Model):
    name_uz = models.CharField(max_length=200, verbose_name='Jurnal nomi (UZ)')
    name_ru = models.CharField(max_length=200, verbose_name='Jurnal nomi (RU)', blank=True, null=True)
    name_en = models.CharField(max_length=200, verbose_name='Jurnal nomi (EN)', blank=True, null=True)
    cover_image = models.ImageField(upload_to='bosh_sahifa/jurnal/jurnal_rasmi', verbose_name='Jurnal old muqovasi rasmi')
    image_2 = models.ImageField(upload_to='bosh_sahifa/jurnal/jurnal_rasmi', verbose_name="Jurnal orqa muqovasi rasmi")
    which_number = models.CharField(max_length=50, verbose_name='Jurnal soni', help_text='Namuna: 1-son | 01.2025')
    slug = models.SlugField(unique=True, verbose_name='Slug', blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Kiritilgan sana')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Yangilangan sana')
    upload_file_uz = models.FileField(upload_to='bosh_sahifa/jurnal/uz', verbose_name='Jurnal faylini yuklash (UZ)', blank=True, null=True)
    upload_file_ru = models.FileField(upload_to='bosh_sahifa/jurnal/ru', verbose_name='Jurnal faylini yuklash (RU)', blank=True, null=True)
    upload_file_en = models.FileField(upload_to='bosh_sahifa/jurnal/en', verbose_name='Jurnal faylini yuklash (RU)', blank=True, null=True)

    class Meta:
        verbose_name = 'Jurnal'
        verbose_name_plural = 'Jurnallar'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(f"{self.which_number}-{self.name_uz}")
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.which_number} - {self.name_uz}"


class ArticleAuthor(models.Model):
    name = models.CharField(max_length=100, verbose_name='Maqola muallifi (UZ)')

    class Meta:
        verbose_name = 'Maqola muallifi'
        verbose_name_plural = 'Maqola mualliflari'

    def __str__(self):
        return self.name


class ArticleCategories(models.Model):
    name_uz = models.CharField(max_length=200, verbose_name='Kategoriya nomi (UZ)')
    name_ru = models.CharField(max_length=200, verbose_name='Kategoriya nomi (RU)', blank=True, null=True)
    name_en = models.CharField(max_length=200, verbose_name='Kategoriya nomi (EN)', blank=True, null=True)
    magazine = models.ForeignKey(Magazine, on_delete=models.CASCADE, related_name='categories', verbose_name='Jurnal soni', blank=True, null=True)

    class Meta:
        verbose_name = 'Maqola kategoriyasi'
        verbose_name_plural = 'Maqola kategoriyalari'

    def __str__(self):
        return self.name_uz


class Article(models.Model):
    magazine = models.ForeignKey(Magazine, on_delete=models.CASCADE, related_name='articles', verbose_name='Jurnali', null=True, blank=True)
    name_uz = models.CharField(max_length=200, verbose_name='Maqola nomi (UZ)')
    name_ru = models.CharField(max_length=200, verbose_name='Maqola nomi (RU)', blank=True, null=True)
    name_en = models.CharField(max_length=200, verbose_name='Maqola nomi (EN)', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Kiritilgan sana')
    category = models.ForeignKey(ArticleCategories, on_delete=models.SET_NULL, null=True, verbose_name='Kategoriya')
    author = models.ForeignKey(ArticleAuthor, on_delete=models.CASCADE, related_name='articles', verbose_name='Muallifi')
    upload_file_uz = models.FileField(upload_to="bosh_sahifa/maqolalar/uz", verbose_name="Maqola fayli (UZ)", blank=True, null=True)
    upload_file_ru = models.FileField(upload_to="bosh_sahifa/maqolalar/ru", verbose_name="Maqola fayli (RU)", blank=True, null=True)
    upload_file_en = models.FileField(upload_to="bosh_sahifa/maqolalar/en", verbose_name="Maqola fayli (EN)", blank=True, null=True)

    class Meta:
        verbose_name = 'Maqola'
        verbose_name_plural = 'Maqolalar'

    def __str__(self):
        return self.name_uz
