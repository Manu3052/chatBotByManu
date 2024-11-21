from rest_framework import serializers

from chat.models import Chat


class ChatSerializer(serializers.ModelSerializer):
    """
    Serializer to convert the Chat model into JSON format.
    """
    class Meta:
        model = Chat
        fields = ['id', 'support_agent_id', 'contact_id', 'start_time', 'closing_time', 'service']
