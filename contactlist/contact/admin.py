from django.contrib import admin

# Register your models here.
from .models import Contact


# Ceci sera affiché dans la partie admin du navigateur
#les champs ci_dessous seront ceux indiqués dans la page

#@admin.register(Contact)

#class ContactModelAdmin(admin.ModelAdmin):
#    list_display = ['full_name', 'relationship','email', 'phone_number', 'address']


admin.site.register(Contact)