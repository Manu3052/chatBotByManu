from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from django.http.response import HttpResponse
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.request import Request
from django.views.decorators.csrf import csrf_exempt

from channels.services.abstract_channel_service import AbstractChannelService
from channels.services.channel_service import ChannelService



# class ChannelViewSet(ModelViewSet):
#     permission_classes = [permissions.AllowAny]

#     def __init__(self, channel_service: AbstractChannelService = ChannelService(), **kwargs):
#         super().__init__(**kwargs)
#         self.channel_service = channel_service

@csrf_exempt
def reply_to_message(request):
    print(request.body)
    return HttpResponse()
