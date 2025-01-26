from django.contrib import admin
from .models import ArticlePreparationGuide, SampleDoc, CopyRight


@admin.register(ArticlePreparationGuide)
class ArticlePreparationGuideAdmin(admin.ModelAdmin):
    list_display = ('id', 'upload_file',)
    search_fields = ('upload_file',)

@admin.register(SampleDoc)
class SampleDocumentAdmin(admin.ModelAdmin):
    list_display = ('id', 'title',)
    search_fields = ('title',)

@admin.register(CopyRight)
class CopyrightAdmin(admin.ModelAdmin):
    list_display = ('id', 'title',)
