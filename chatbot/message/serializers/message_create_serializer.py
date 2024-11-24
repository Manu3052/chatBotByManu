from rest_framework import serializers
from chat.models import Chat
from contact.models import Contact
from message.models import Message


class MessageCreateSerializer(serializers.ModelSerializer):
    chat_id = serializers.PrimaryKeyRelatedField(
        queryset=Chat.objects.all(),
        required=True,
    )
    sender = serializers.SerializerMethodField()

    class Meta:
        model = Message
        fields = [
            'id',
            'chat_id',
            'sender_type',
            'message_content',
            'sender',
        ]

    def to_internal_value(self, data):
        """
        Valida e transforma os dados de entrada em um formato interno.
        """
        if not isinstance(data, dict):
            raise serializers.ValidationError("Os dados devem estar no formato de dicionário.")

        message_content = data.get('message', {}).get('text')
        if not message_content:
            raise serializers.ValidationError({"message_content": "O conteúdo da mensagem não pode estar vazio."})

        is_bot = data.get('message', {}).get('from', {}).get('is_bot', False)
        sender_type = 2 if is_bot else 1

        chat = data.get('chat_id')
        if not chat:
            raise serializers.ValidationError({"chat": "O ID do chat é obrigatório."})
        if sender_type == 1:
            contact = Contact.objects.create(name=message_content)

        message_data = {
            "sender": contact,
            "message_content": message_content,
            "chat_id": chat,
            "sender_type": sender_type,
        }

        return message_data