from django.contrib import admin
from .models import Chat

@admin.register(Chat)
class ChatAdmin(admin.ModelAdmin):
    """
    Admin configuration for the Chat model.
    Displays 'id', 'support_agent_id', 'contact_id', 'start_time', 'closing_time', and 'service' in the list view.
    """
    list_display = ('id', 'support_agent_id', 'contact_id', 'start_time', 'closing_time', 'service')
    search_fields = ('support_agent_id__name', 'contact_id__name', 'service')
