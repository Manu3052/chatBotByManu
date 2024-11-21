from django.contrib import admin

from .models import SupportAgent


@admin.register(SupportAgent)
class SupportAgentAdmin(admin.ModelAdmin):
    """
    Admin interface for the SupportAgent model.

    Features:
        - Displays fields in the list view.
        - Adds search functionality for first and last names.
        - Filters by first and last names.
    """
    list_display = ("id", "first_name", "last_name")
    search_fields = ("first_name", "last_name")
    list_filter = ("first_name", "last_name")
