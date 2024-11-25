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

from chat.providers.telegram_provider import TelegramProvider
from chat.serializers.chat_serializer import ChatSerializer
from chat.serializers.telegram_input_serializer import TelegramInputSerializer
from chat.services.abstract_channel_service import AbstractChannelService
from chat.services.channel_service import ChannelService
from chat.utils.bot_validator import BotValidator
from contact.services.contact_service import ContactService
from contact.services.abstract_contact_service import AbstractContactService
from message.serializers.message_create_serializer import \
    MessageCreateSerializer
from message.services.abstract_message_service import AbstractMessageService
from message.services.message_service import MessageService
from supportAgent.views import SupportAgentService


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

    def __init__(self, channel_service: AbstractChannelService = ChannelService(), message_service: AbstractMessageService = MessageService(), contact_service: AbstractContactService= ContactService(), support_agent=  SupportAgentService(), **kwargs):
        """
        Initializes the ChannelViewSet with a channel service.
        
        Args:
            channel_service (AbstractChannelService, optional): The service used to manage channels.
            message_service (AbstractMessageService, optional): The service used to manage messages.
        """
        self.channel_service = channel_service
        self.message_service = message_service
        self.contact_service = contact_service
        self.support_agent_service = support_agent

    @method_decorator(csrf_exempt, name="dispatch")
    @action(detail=False, methods=["post"], url_path="receive-messages")
    def receive_messages(self, request):
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
                if not data.get('callback_query'):
                    contact_name = data['message']['chat']['first_name']
                    contact = self.contact_service.get_contact_by_name_intern(contact_name)
                    if not contact:
                        contact = self.contact_service.create({"name":contact_name})
                telegram_answer = TelegramProvider()
                serializer_class = TelegramInputSerializer
                serializer = serializer_class(data=data, context={"request": data})
                serializer.is_valid(raise_exception=True)
                chat_instance = self.channel_service.create(serializer.validated_data)
                if not data.get('callback_query'):
                    message_serializer_class = MessageCreateSerializer
                    data['chat_id'] = chat_instance
                    message_serializer = message_serializer_class(data=data)
                    message_serializer.is_valid(raise_exception=True)
                    message = self.message_service.create(message_serializer.validated_data)
                    data= json.loads(request.body)
                    telegram_answer.setup_handlers(data=data, message=message.message_content)
                elif data.get('callback_query'):
                    telegram_answer.setup_handlers(data=data)
            return Response({"message_received": True}, status=status.HTTP_200_OK)
        except ValidationError as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    @method_decorator(csrf_exempt, name="dispatch")
    @action(detail=False, methods=["post"], url_path=r"answer-messages/(?P<chat_id>.+)")
    def answer_messages(self, request, chat_id: int):
        try:
            bot_name =  request.data['bot_name']
            if bot_name == "telegram":
                serializer_class =  MessageCreateSerializer
                support_agent = request.data['support_agent']
                support_agent = self.support_agent_service.get_by_id(support_agent)
                answer = request.data['answer']
                self.message_service.create()
                telegram_answer = TelegramProvider()
                telegram_answer.reply(chat_id, answer)
            return Response({"message_send": True}, status=status.HTTP_200_OK)
        except ValidationError as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
