import json

from django.http import HttpResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from rest_framework import permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from chat.serializers.chat_serializer import ChatSerializer
from chat.services.abstract_channel_service import AbstractChannelService
from chat.services.channel_service import ChannelService


class ChannelViewSet(ModelViewSet):
    permission_classes = [permissions.AllowAny]
    serializer_class = ChatSerializer
    queryset = None

    def __init__(self, channel_service: AbstractChannelService = ChannelService(), **kwargs):
        super().__init__(**kwargs)
        self.channel_service = channel_service

    @method_decorator(csrf_exempt, name="dispatch")
    @action(detail=False, methods=["post"], url_path="reply-to-message")
    def reply_to_message(self, request):
        try:
            data = json.loads(request.body)
            message_text = data.get("message", {}).get("text", "")
            print(message_text)
            return Response({"message_received": message_text}, status=status.HTTP_200_OK)
        except (json.JSONDecodeError, KeyError) as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
