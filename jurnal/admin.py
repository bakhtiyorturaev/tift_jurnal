from django.contrib import admin
from .forms import AboutMagazineForm, MagazineRequirementsForm
from .models import AboutMagazine, MagazineNews, MagazineRequirements, Statistics


@admin.register(AboutMagazine)
class AboutMagazineAdmin(admin.ModelAdmin):
    form = AboutMagazineForm
    list_display = ('magazine', 'magazine_name_uz', 'magazine_name_ru', 'magazine_name_en')



@admin.register(MagazineNews)
class MagazineNewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'magazine', 'title_uz', 'link')
    list_filter = ('magazine',)
    search_fields = ('title_uz', 'content_uz')
    ordering = ('-id',)

@admin.register(MagazineRequirements)
class MagazineRequirementsAdmin(admin.ModelAdmin):
    form = MagazineRequirementsForm
    list_display = ('id', 'title_uz', 'title_ru', 'title_en')
    search_fields = ('title_uz', 'title_ru', 'title_en')
    ordering = ('-id',)


@admin.register(Statistics)
class StatisticsAdmin(admin.ModelAdmin):
    list_display = ('id', 'magazine', 'magazine_info', 'articles_count', 'updated_at')
    readonly_fields = ('magazine_info', 'articles_count', 'created_at', 'updated_at')

    @admin.display(description="Magazine Info")
    def magazine_info(self, obj):
        return obj.magazine_info()

    @admin.display(description="Articles Count")
    def articles_count(self, obj):
        return obj.articles_count()


