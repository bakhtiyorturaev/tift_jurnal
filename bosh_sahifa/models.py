from django.db import models

class Magazine(models.Model):
    name = models.CharField(max_length=200, verbose_name='jurnal nomi')
    cover_image = models.ImageField(upload_to='bosh_sahifa/jurnal/jurnal_rasmi', verbose_name='jurnal old muqovasi rasmi')
    image_2 = models.ImageField(upload_to='bosh_sahifa/jurnal/jurnal_rasmi', verbose_name="jurnal orqa muqovasi rasmi ")
    which_number = models.CharField(max_length=50, verbose_name='jurnal soni')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='kirtilayotgan sana')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='yangilangan sana')
    upload_file = models.FileField(upload_to='bosh_sahifa/jurnal', verbose_name='jurnal faylini yuklash')

    class Meta:
        verbose_name = 'Jurnal'
        verbose_name_plural = 'Jurnallar'

    def __str__(self):
        return self.name


class ArticleAuthor(models.Model):
    name = models.CharField(max_length=100, verbose_name='Maqola muallifi')


    class Meta:
        verbose_name = 'Maqola muallifi'
        verbose_name_plural = 'Maqola mualliflari'

    def __str__(self):
        return self.name



class ArticleCategories(models.Model):
    name = models.CharField(max_length=200, verbose_name='Kategoriya nomi')

    class Meta:
        verbose_name = 'Maqola kategoriyasi'
        verbose_name_plural = 'Maqola kategoriyalari'

    def __str__(self):
        return self.name


class Article(models.Model):
    name = models.CharField(max_length=200, verbose_name='Maqola nomi')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Kiritilayotgan sana')
    category = models.ForeignKey(ArticleCategories, on_delete=models.SET_NULL, null=True, verbose_name='Kategoriiyasi')
    author = models.ForeignKey(ArticleAuthor, on_delete=models.CASCADE, related_name='articles', verbose_name='Muallifi')
    upload_file = models.FileField(upload_to="bosh_sahifa/maqolalar/", verbose_name='Maqola fayli')

    class Meta:
        verbose_name = 'Maqola'
        verbose_name_plural = 'Maqolalar'

    def __str__(self):
        return self.name


