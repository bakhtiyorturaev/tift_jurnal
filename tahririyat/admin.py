from django.contrib import admin
from .models import EditorialMember, EditorialStaff, HonoraryForeignEditorialMember, ForeignEditorialMember


@admin.register(EditorialMember)
class EditorialBoardAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'title_1',)
    search_fields = ('name', 'title_1',)

@admin.register(EditorialStaff)
class EditorialStaffAdmin(admin.ModelAdmin):
    list_display = ('id',)

@admin.register(HonoraryForeignEditorialMember)
class HonoraryForeignEditorialMemberAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)
    search_fields = ('name',)


@admin.register(ForeignEditorialMember)
class ForeignEditorialMemberAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)
    search_fields = ('name',)