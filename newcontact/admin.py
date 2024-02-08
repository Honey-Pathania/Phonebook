from django.contrib import admin
from newcontact.models import Phonebook


class AdminContact(admin.ModelAdmin):
    list_display = ['Name', 'Contact']

admin.site.register(Phonebook, AdminContact)
