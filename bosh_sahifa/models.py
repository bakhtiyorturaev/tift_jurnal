from django.db import models
from django.utils.text import slugify
from django.urls import reverse

class Magazine(models.Model):
    name = models.CharField(max_length=200, verbose_name='jurnal nomi')
    cover_image = models.ImageField(upload_to='bosh_sahifa/jurnal/jurnal_rasmi', verbose_name='jurnal old muqovasi rasmi')
    image_2 = models.ImageField(upload_to='bosh_sahifa/jurnal/jurnal_rasmi', verbose_name="jurnal orqa muqovasi rasmi ")
    slug = models.SlugField(max_length=200, unique=True, blank=True, )
    which_number = models.CharField(max_length=50, verbose_name='jurnal soni')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='kirtilayotgan sana')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='yangilangan sana')
    upload_file = models.FileField(upload_to='bosh_sahifa/jurnal', verbose_name='jurnal faylini yuklash')

    class Meta:
        verbose_name = 'Jurnal'
        verbose_name_plural = 'Jurnallar'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('magazine-detail', kwargs={'slug': self.slug})


class ArticleAuthor(models.Model):
    name = models.CharField(max_length=100, verbose_name='Maqola muallifi')
    slug = models.SlugField(max_length=200, blank=True, unique=True, verbose_name='Slug')


    class Meta:
        verbose_name = 'Maqola muallifi'
        verbose_name_plural = 'Maqola mualliflari'


    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name



class ArticleCategories(models.Model):
    name = models.CharField(max_length=100, verbose_name='Kategoriya nomi')
    slug = models.SlugField(max_length=100, blank=True, unique=True)

    class Meta:
        verbose_name = 'Maqola kategoriyasi'
        verbose_name_plural = 'Maqola kategoriyalari'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category-detail', kwargs={'slug': self.slug})


class Article(models.Model):
    name = models.CharField(max_length=200, verbose_name='Maqola nomi')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Kiritilayotgan sana')
    category = models.ForeignKey(ArticleCategories, on_delete=models.SET_NULL, null=True, verbose_name='Kategoriiyasi')
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    author = models.ForeignKey(ArticleAuthor, on_delete=models.CASCADE, related_name='articles', verbose_name='Muallifi')
    upload_file = models.FileField(upload_to="bosh_sahifa/maqolalar/", verbose_name='Maqola fayli')

    class Meta:
        verbose_name = 'Maqola'
        verbose_name_plural = 'Maqolalar'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('article-detail', kwargs={'slug': self.slug})

