from django.contrib import admin
from .models import EditorialStaff, HonoraryForeignEditorialMember, ForeignEditorialMember
from .forms import EditorialStaffForm

@admin.register(EditorialStaff)
class EditorialStaffAdmin(admin.ModelAdmin):
    form = EditorialStaffForm
    list_display = ['id', 'content_uz', 'content_ru', 'content_en']

#
# @admin.register(HonoraryForeignEditorialMember)
# class HonoraryForeignEditorialMemberAdmin(admin.ModelAdmin):
#     list_display = ('id', 'name',)
#     search_fields = ('name',)
#
#
# @admin.register(ForeignEditorialMember)
# class ForeignEditorialMemberAdmin(admin.ModelAdmin):
#     list_display = ('id', 'name',)
#     search_fields = ('name',)