from django.contrib import admin
from .models import EditorialMember, EditorialStaff, HonoraryForeignEditorialMember, ForeignEditorialMember
from .forms import EditorialStaffForm

@admin.register(EditorialMember)
class EditorialBoardAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'title_1_uz',)
    search_fields = ('name', 'title_1_uz',)

@admin.register(EditorialStaff)
class EditorialStaffAdmin(admin.ModelAdmin):
    form = EditorialStaffForm
    list_display = ('id',)

@admin.register(HonoraryForeignEditorialMember)
class HonoraryForeignEditorialMemberAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)
    search_fields = ('name',)


@admin.register(ForeignEditorialMember)
class ForeignEditorialMemberAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)
    search_fields = ('name',)