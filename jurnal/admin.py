from django.contrib import admin
from .models import AboutMagazine, MagazineNews, MagazineRequirements, MagazineArchive


@admin.register(AboutMagazine)
class AboutMagazineAdmin(admin.ModelAdmin):
    list_display = ['magazine', 'slug', 'bio']
    search_fields = ['magazine__name', 'slug']

@admin.register(MagazineNews)
class MagazineNewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'magazine', 'title', 'link')
    list_filter = ('magazine',)
    search_fields = ('title', 'content')
    ordering = ('-id',)

@admin.register(MagazineRequirements)
class MagazineRequirementsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    search_fields = ('title', 'content')
    ordering = ('-id',)

@admin.register(MagazineArchive)
class MagazineArchiveAdmin(admin.ModelAdmin):
    list_display = ('id',)
    search_fields = ('content',)
    ordering = ('-id',)

class StatisticsAdmin(admin.ModelAdmin):
    list_display = ('id', 'magazine', 'magazine_info', 'articles_count', 'updated_at')
    readonly_fields = ('magazine_info', 'articles_count', 'created_at', 'updated_at')

    def magazine_info(self, obj):
        return obj.magazine_info()

    def articles_count(self, obj):
        return obj.articles_count()

