from django.contrib import admin
from .models import AboutMagazine, MagazineNews, MagazineRequirements, MagazineArchive, MagazineStatistics


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

@admin.register(MagazineStatistics)
class MagazineStatisticsAdmin(admin.ModelAdmin):
    list_display = ('id', 'content')

