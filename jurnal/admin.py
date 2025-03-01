from django.contrib import admin
from .forms import AboutMagazineForm, MagazineRequirementsForm
from .models import AboutMagazine, MagazineNews, MagazineRequirements, Statistics


@admin.register(AboutMagazine)
class AboutMagazineAdmin(admin.ModelAdmin):
    list_display = ["name", "language"]
    list_filter = ["language"]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        """Jurnal tanlashda faqat mos keladigan tildagi jurnallarni chiqarish"""
        if db_field.name == "magazine":
            lang = request.GET.get("language")
            if lang:
                kwargs["queryset"] = AboutMagazine(language=lang).get_filtered_magazines()

        return super().formfield_for_foreignkey(db_field, request, **kwargs)

    def get_fields(self, request, obj=None):
        """Tanlangan tilga qarab maydonlarni moslashtirish"""
        fields = ["magazine", "language"]
        if obj:
            if obj.language == "uz":
                fields += ["bio_uz", "file_uz"]
            elif obj.language == "ru":
                fields += ["bio_ru", "file_ru"]
            elif obj.language == "en":
                fields += ["bio_en", "file_en"]
        return fields



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

