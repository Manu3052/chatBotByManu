from message.models import Message
from rest_framework import serializers


class MessageListSerializer(serializers.ModelSerializer):
    """
    Serializer for the Message model.

    Purpose:
        - Converts Message model instances to JSON format (serialization).
        - Validates and creates Message model instances from JSON data (deserialization).

    Fields:
        - id (int): Auto-generated unique identifier for the message (primary key, inherited from the model).
        - chat_id (int): ForeignKey reference to the related Chat instance.
        - sender_type (int): The type of sender for the message (1 = USER, 2 = BOT, 3 = SUPPORT_AGENT).
        - message_content (str): The content of the message (required).
        - created_at (datetime): Timestamp of when the message was created (default is current time).
    """

    sender_type_display = serializers.CharField(source='get_sender_type_display', read_only=True)

    class Meta:
        """
        Meta configuration for the MessageSerializer.

        Attributes:
            - model (Message): Specifies the model class that this serializer corresponds to.
            - fields (list): Defines the fields to be included in the serialized output or deserialized input.
        """
        model = Message
        fields = [
            'id',
            'chat_id_id',
            'sender_type',
            'sender_type_display',
            'message_content',
            'created_at',
        ]
