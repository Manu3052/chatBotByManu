from rest_framework import serializers

from chat.models import Chat


class TelegramInputSerializer(serializers.ModelSerializer):
    """
    Serializer for the Chat model.
    Converts Chat model instances to JSON format and vice versa.
    Fields:
        - id: Auto-generated unique identifier for the chat.
        - chat: Identifier of the chat from the external service (if any).
        - contact_id: ID of the contact participating in the chat.
        - service: The external service used (e.g., Telegram, Discord).
    """
    class Meta:
        model = Chat
        fields = [
            'id',
            'chat',
            'contact_id',
            'service'
        ]

    def to_internal_value(self, data: dict):
        """
        Customizes the deserialization process by injecting additional fields or transforming input data.
        
        Args:
            - data (dict): The incoming data dictionary to be deserialized.

        Returns:
            - dict: The modified data dictionary, which will then be passed to the default deserialization logic.

        Custom Logic:
            - Extracts the `chat_id` from the 'chat' key in the input data.
            - Maps the `id` field in the input data to `contact_id` for compatibility with the Chat model.
            - Sets the `service` field to '0' (defaulting to Telegram).
        """
        data = data['message']
        data['chat']= data['from']['id']
        data['service']='0'
        return super().to_internal_value(data)