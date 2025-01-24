from django.db import models
from django.utils.text import slugify
from django.urls import reverse
from django_ckeditor_5.fields import CKEditor5Field

class Magazine(models.Model):
    name = models.CharField(max_length=200)
    cover_image = models.ImageField(upload_to='bosh_sahifa/jurnal/jurnal_rasmi')
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    which_number = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    bio = CKEditor5Field(config_name='read_only') # Jurnalning orqa tomoni uchun ma'lumot
    upload_file = models.FileField(upload_to='bosh_sahifa/jurnal')

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('magazine-detail', kwargs={'slug': self.slug})


class ArticleAuthor(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=200, blank=True, unique=True)



class ArticleCategories(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, blank=True, unique=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category-detail', kwargs={'slug': self.slug})


class Article(models.Model):
    name = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(ArticleCategories, on_delete=models.SET_NULL, null=True)
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    author = models.ForeignKey(ArticleAuthor, on_delete=models.CASCADE, related_name='articles')
    upload_file = models.FileField(upload_to="bosh_sahifa/maqolalar/")

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('article-detail', kwargs={'slug': self.slug})

