from django.contrib import admin
from .models import Magazine, Article, ArticleAuthor, ArticleCategories

@admin.register(Magazine)
class MagazineAdmin(admin.ModelAdmin):
    list_display = ('name_uz', 'which_number', 'created_at')
    search_fields = ('name_uz', 'created_at')


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('name_uz', 'created_at', 'author')  # Ko‘rinadigan maydonlar
    search_fields = ('name_uz', 'author__name')  # Qidiruv nom va muallif nomi bo‘yicha
    list_filter = ('category', 'created_at')  # Filtrlash imkoniyatlari

@admin.register(ArticleAuthor)
class ArticleAuthorAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(ArticleCategories)
class ArticleCategoriesAdmin(admin.ModelAdmin):
    list_display = ('name_uz',)
    search_fields = ('name_uz',)
