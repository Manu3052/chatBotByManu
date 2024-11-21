from django.contrib import admin

from .models import Contact


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    """
    Admin configuration for the Contact model.
    Displays 'id', 'name', 'email', 'cpf', and 'telephone' in the list view.
    Allows searching by 'name', 'email', 'cpf', and 'telephone'.
    """
    list_display = ('id', 'name', 'email', 'cpf', 'telephone')
    search_fields = ('name', 'email', 'cpf', 'telephone')
