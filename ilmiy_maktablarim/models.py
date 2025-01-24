from django.db import models
from django.utils.text import slugify
from django_ckeditor_5.fields import CKEditor5Field


class IlmiyMaktablarim(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='ilmiy_maktablarimiz/')
    academic_degree = models.CharField(max_length=200)
    bio = CKEditor5Field(config_name='extends')
    slug = models.SlugField(max_length=200, unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

