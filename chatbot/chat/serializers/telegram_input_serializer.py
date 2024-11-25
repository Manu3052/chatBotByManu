from rest_framework import serializers
from chat.models import Chat
from contact.models import Contact


class TelegramInputSerializer(serializers.ModelSerializer):
    """
    Serializer for the Chat model.
    Converts Chat model instances to JSON format and vice versa.
    """
    contact_id = serializers.PrimaryKeyRelatedField(
        queryset=Contact.objects.all(),
        required=True,
    )
    class Meta:
        model = Chat
        fields = [
            'id',
            'chat',
            'service',
            'contact_id',
        ]

    def to_internal_value(self, data: dict):
        """
        Customizes the deserialization process by injecting additional fields or transforming input data.
        
        Args:
            - data (dict): The incoming data dictionary to be deserialized.

        Returns:
            - dict: The modified data dictionary, which will then be passed to the default deserialization logic.

        Custom Logic:
            - Handles two formats: `message` and `callback_query`.
            - Extracts `chat_id` from the appropriate location based on the input format.
            - Maps `contact_id` and sets `service` based on the data.
        """
        if 'message' in data:
            message = data['message']
            data['chat'] = message['from']['id'] 
            data['service'] = '0' 
            name = message['chat']['first_name']
            contact= Contact.objects.filter(name=name).first()
            data['contact_id'] = contact.id
        elif 'callback_query' in data:
            callback_query = data['callback_query']
            message = callback_query['message']
            data['chat'] = message['from']['id'] 
            name = message['chat']['first_name']
            contact = Contact.objects.filter(name=name).first()
            data['contact_id'] = contact.id
            data['service'] = '0' 
        else:
            raise serializers.ValidationError("Invalid data structure, must contain 'message' or 'callback_query'.")

        return super().to_internal_value(data)
