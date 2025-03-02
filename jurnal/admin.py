from django.contrib import admin
from .forms import AboutMagazineForm, MagazineRequirementsForm
from .models import AboutMagazine, MagazineNews, MagazineRequirements, Statistics


from django.contrib import admin
from .models import AboutMagazine

@admin.register(AboutMagazine)
class AboutMagazineAdmin(admin.ModelAdmin):
    list_display = ('get_magazine_name_uz', 'get_magazine_name_ru', 'get_magazine_name_en')

    def get_magazine_name_uz(self, obj):
        return obj.magazine.name_uz if obj.magazine else "Noma'lum"
    get_magazine_name_uz.short_description = "Jurnal nomi (UZ)"

    def get_magazine_name_ru(self, obj):
        return obj.magazine.name_ru if obj.magazine else "Noma'lum"
    get_magazine_name_ru.short_description = "Jurnal nomi (RU)"

    def get_magazine_name_en(self, obj):
        return obj.magazine.name_en if obj.magazine else "Noma'lum"
    get_magazine_name_en.short_description = "Jurnal nomi (EN)"



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


