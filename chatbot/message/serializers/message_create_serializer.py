from rest_framework import serializers
from chat.models import Chat
from message.models import Message


class MessageCreateSerializer(serializers.ModelSerializer):
    chat = serializers.PrimaryKeyRelatedField(
        queryset=Chat.objects.all(),
        required=True,
    )
    class Meta:
        model = Message
        fields = [
            'id',
            'chat',
            'sender_type',
            'message_content',
        ]

    def to_internal_value(self, data: dict):
        if not isinstance(data, dict):
            raise serializers.ValidationError("Os dados devem estar no formato de dicionário.")

        sender_type = 2 if data['message']['from']['is_bot'] else 1

        message_content = data.get('message', {}).get('text')
        if not message_content:
            raise serializers.ValidationError({"message_content": "O conteúdo da mensagem não pode estar vazio."})

        chat = data.get('chat')
        if not chat:
            raise serializers.ValidationError({"chat": "O ID do chat é obrigatório."})

        data = {
            'message_content': message_content,
            'chat': chat,
            'sender_type': sender_type,
        }
        return super().to_internal_value(data)
