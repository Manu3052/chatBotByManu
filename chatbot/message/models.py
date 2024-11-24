from django.db import models
from django.utils import timezone
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

from chat.models import Chat


class Message(models.Model):
    """
    A model representing a message in a chat system.
    
    Attributes:
        id (int): The unique identifier for the message (Primary Key).
        chat_id(ForeignKey): A reference to the chat this message belongs to (Foreign Key to Chat model, with cascade deletion).
        sender_type (int): Indicates the sender of the message (1 = USER, 2 = BOT, 3 = SUPPORT_AGENT).
        message_content (str): The content of the message (cannot be null).
        created_at (datetime): The date and time when the message was created (default: current timestamp).
        updated_at (datetime): The date and time when the message was last updated (optional, for edited messages).
    """
    
    chat_id = models.ForeignKey(Chat, on_delete=models.CASCADE, related_name='messages', help_text="The chat to which this message belongs.")
    sender_type = models.IntegerField(
        choices=[(1, 'User'), (2, 'Bot'), (3, 'Support Agent')],
        default=1,
        help_text="The type of sender for the message (1 = USER, 2 = BOT, 3 = SUPPORT_AGENT)."
    )
    message_content = models.TextField(help_text="The content of the message (cannot be null).")
    created_at =models.DateTimeField(default=timezone.now)
    sender_content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, null=True, blank=False)
    sender_object_id = models.PositiveIntegerField(null=True, blank=False)
    sender = GenericForeignKey('sender_content_type', 'sender_object_id')
    class Meta:
        verbose_name = "Message"
        verbose_name_plural = "Messages"
        ordering = ['created_at']

    def __str__(self):
        """
        Returns a string representation of the message, including the sender type and a preview of the message content.
        """
        return f"{self.get_sender_type_display()}: {self.message_content[:50]}..."
