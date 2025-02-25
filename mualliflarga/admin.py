from django.contrib import admin
from .models import ArticlePreparationGuide, SampleDoc, CopyRight
from .forms import SampleDocForm, CopyRightForm

@admin.register(ArticlePreparationGuide)
class ArticlePreparationGuideAdmin(admin.ModelAdmin):
    list_display = ('id', 'upload_file_uz',)
    search_fields = ('upload_file_uz',)

@admin.register(SampleDoc)
class SampleDocumentAdmin(admin.ModelAdmin):
    form = SampleDocForm
    list_display = ('id', 'title_uz', 'title_ru')
    search_fields = ('title_uz', 'title_ru')

@admin.register(CopyRight)
class CopyrightAdmin(admin.ModelAdmin):
    form = CopyRightForm
    list_display = ('id', 'title_uz',)
