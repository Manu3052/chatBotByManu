import json

from django.http import HttpResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from rest_framework import permissions, status
from rest_framework.decorators import action
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from chat.models import Chat

from chat.serializers.chat_serializer import ChatSerializer
from chat.serializers.telegram_input_serializer import TelegramInputSerializer
from chat.services.abstract_channel_service import AbstractChannelService
from chat.services.channel_service import ChannelService
from chat.utils.bot_validator import BotValidator
from message.serializers.message_create_serializer import \
    MessageCreateSerializer
from message.services.abstract_message_service import AbstractMessageService
from message.services.message_service import MessageService


class ChannelViewSet(ModelViewSet):
    """
    Viewset for managing communication channels.
    
    This viewset allows creation and management of channels, with the ability 
    to handle incoming messages from different bots (e.g., Telegram, Discord).
    
    Methods:
        create: Handle incoming messages and create chats or messages based on bot type.
    """
    
    permission_classes = [permissions.AllowAny]
    serializer_class = ChatSerializer
    queryset = Chat.objects.all()

    def __init__(self, channel_service: AbstractChannelService = ChannelService(), message_service: AbstractMessageService = MessageService(), **kwargs):
        """
        Initializes the ChannelViewSet with a channel service.
        
        Args:
            channel_service (AbstractChannelService, optional): The service used to manage channels.
            message_service (AbstractMessageService, optional): The service used to manage messages.
        """
        self.channel_service = channel_service
        self.message_service = message_service

    @method_decorator(csrf_exempt, name="dispatch")
    @action(detail=False, methods=["post"], url_path="reply-to-message")
    def reply_to_message(self, request):
        """
        Handle incoming messages from various bots (e.g., Telegram, Discord).
        
        Depending on the bot type, a chat or message is created.
        
        Args:
            request (Request): The request containing the message data.
            
        Returns:
            Response: The response with the status of the operation.
        """
        try:
            data = json.loads(request.body)
            bot_validator = BotValidator()
            bot_name = bot_validator.identify_bot(request.body)
            if bot_name == 'unknown':
                raise ValidationError("This bot is not supported.")
            elif bot_name == "telegram":
                serializer_class = TelegramInputSerializer
                serializer = serializer_class(data=data, context={"request": data})
                serializer.is_valid(raise_exception=True)
                chat_instance = self.channel_service.create(serializer.validated_data)
                message_serializer_class = MessageCreateSerializer
                data['chat_id'] = chat_instance
                message_serializer = message_serializer_class(data=data)
                message_serializer.is_valid(raise_exception=True)
                self.message_service.create(message_serializer.validated_data)  
            return Response({"message_received": True}, status=status.HTTP_200_OK)
        except ValidationError as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
