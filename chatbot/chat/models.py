from django.db import models
from django.utils import timezone

from contact.models import Contact
from supportAgent.models import SupportAgent


class Chat(models.Model):
    """
    Model to store chat information.
    Fields:
        - id: Unique identifier for each chat (Primary Key).
        - support_agent_id: ForeignKey reference to the support agent (with cascade deletion).
        - contact_id: ForeignKey reference to the contact involved (with cascade deletion).
        - start_time: Timestamp of the chat's start time (default: current timestamp).
        - closing_time: Timestamp of the chat's closing time (optional).
        - service: The service used for the chat (e.g., 'telegram', 'wpp').
    """
    id = models.AutoField(primary_key=True)
    chat_id = models.CharField(max_length=150, null=True, blank=True)
    support_agent_id = models.ForeignKey(
        SupportAgent, on_delete=models.CASCADE, related_name='support_chats', null=True, blank=True
    )
    contact_id = models.ForeignKey(
        Contact, on_delete=models.CASCADE, related_name='contact_chats', null=True, blank=True
    )
    start_time = models.DateTimeField(default=timezone.now)
    closing_time = models.DateTimeField(null=True, blank=True)
    service = models.CharField(max_length=2, choices=[('0', 'Telegram'), ('1', 'Discord')])

    def __str__(self):
        """
        Return a string representation of the chat, showing the chat id and service.
        """
        return f"Chat {self.id} ({self.service}{self.support_agent_id}{self.contact_id})"
