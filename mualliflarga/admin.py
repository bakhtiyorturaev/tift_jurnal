from django.contrib import admin
from .models import ArticlePreparationGuide, SampleDoc, CopyRight
from .forms import SampleDocForm, CopyRightForm, ArticlePreparationGuideForm

@admin.register(ArticlePreparationGuide)
class ArticlePreparationGuideAdmin(admin.ModelAdmin):
    form = ArticlePreparationGuideForm
    list_display = ['id']
    search_fields = ['yuriqnoma_uz', 'yuriqnoma_ru', 'yuriqnoma_en']

@admin.register(SampleDoc)
class SampleDocumentAdmin(admin.ModelAdmin):
    form = SampleDocForm
    list_display = ('id', 'title_uz', 'title_ru')
    search_fields = ('title_uz', 'title_ru')

@admin.register(CopyRight)
class CopyrightAdmin(admin.ModelAdmin):
    form = CopyRightForm
    list_display = ('id', 'title_uz',)
