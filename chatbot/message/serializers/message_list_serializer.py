from models import Message
from rest_framework import serializers


class MessageListSerializer(serializers.ModelSerializer):
    """
    Serializer for the Message model.

    Purpose:
        - Converts Message model instances to JSON format (serialization).
        - Validates and creates Message model instances from JSON data (deserialization).

    Fields:
        - id (int): Auto-generated unique identifier for the message (primary key, inherited from the model).
        - chat (int): ForeignKey reference to the related Chat instance.
        - sender_type (int): The type of sender for the message (1 = USER, 2 = BOT, 3 = SUPPORT_AGENT).
        - message_content (str): The content of the message (required).
        - created_at (datetime): Timestamp of when the message was created (default is current time).
        - updated_at (datetime): Timestamp of the last update to the message (optional).
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
            'chat',
            'sender_type',
            'sender_type_display',
            'message_content',
            'created_at',
            'updated_at'
        ]

    def validate_message_content(self, value):
        """
        Validates the `message_content` field to ensure it is not empty.

        Args:
            - value (str): The content of the message provided by the user.

        Returns:
            - str: The validated content.

        Raises:
            - serializers.ValidationError: If the `message_content` is empty or only contains whitespace.
        """
        if not value.strip():
            raise serializers.ValidationError("Message content cannot be empty.")
        return value
