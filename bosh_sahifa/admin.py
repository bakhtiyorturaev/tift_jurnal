from django.contrib import admin
from django import forms
from django_ckeditor_5.widgets import CKEditor5Widget
from .models import Magazine, Article, ArticleAuthor, ArticleCategories

class MagazineAdminForm(forms.ModelForm):

    class Meta:
        model = Magazine
        fields = '__all__'  # yoki kerakli boshqa fieldlar
        widgets = {
            "bio": CKEditor5Widget(
                attrs={"class": "django_ckeditor_5"}, config_name='default'
            )
        }

@admin.register(Magazine)
class MagazineAdmin(admin.ModelAdmin):
    form = MagazineAdminForm
    list_display = ('name', 'which_number', 'created_at')
    search_fields = ('name', 'created_at')

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at', 'author')  # Ko‘rinadigan maydonlar
    search_fields = ('name', 'author__name')  # Qidiruv nom va muallif nomi bo‘yicha
    list_filter = ('category', 'created_at')  # Filtrlash imkoniyatlari

@admin.register(ArticleAuthor)
class ArticleAuthorAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(ArticleCategories)
class ArticleCategoriesAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
