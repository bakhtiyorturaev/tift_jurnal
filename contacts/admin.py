from django.contrib import admin
from .models import Contacts

@admin.register(Contacts)
class ContactsAdmin(admin.ModelAdmin):
    list_display = ['phone_numbers', 'fax_number', 'email', 'address_uz', 'image']
