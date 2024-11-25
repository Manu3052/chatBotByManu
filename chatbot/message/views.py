import json

from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from rest_framework import permissions, status
from rest_framework.decorators import action
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from message.utils.pagination import PaginatorConfig

from message.models import Message
from message.serializers.message_create_serializer import \
    MessageCreateSerializer
from message.serializers.message_list_serializer import MessageListSerializer
from message.services.message_service import MessageService


class MessageViewSet(ModelViewSet):
    """
    Viewset for handling incoming messages from various bots (e.g., Telegram, Discord).
    
    This viewset is responsible for processing messages and creating corresponding message records.
    
    Methods:
        create: Handle incoming messages and store them in the database.
        update: Update an existing message.
        list: List all messages.
        delete: Delete a message by ID.
    """
    
    permission_classes = [permissions.AllowAny]
    serializer_class = MessageCreateSerializer
    queryset = Message.objects.all()
    pagination_class= PaginatorConfig

    
    def get_serializer_class(self):
        if self.action == "create":
            return MessageListSerializer
        elif self.action == "list":
            return MessageListSerializer
        elif self.action == "get_by_contact":
            return MessageListSerializer
        elif self.action == "get_by_support_agent":
            return MessageListSerializer

        return MessageListSerializer

    def __init__(self, message_service: MessageService = MessageService(), **kwargs):
        """
        Initializes the MessageViewSet with the message service.
        
        Args:
            message_service (MessageService, optional): The service used to handle message logic.
        """
        super().__init__(**kwargs)
        self.message_service = message_service

    @method_decorator(csrf_exempt, name="dispatch")
    def create(self, request) -> Response:
        """
        Handle incoming messages from bots and create corresponding message records.
        
        Args:
            request (Request): The request containing the message data.
            
        Returns:
            Response: The response with the status of the operation.
        """
        try:
            data = json.loads(request.body)
            self.message_service.create(data)
            return Response({"message_received": True}, status=status.HTTP_200_OK)
        
        except (json.JSONDecodeError, KeyError) as e:
            return Response({"error": f"Invalid data format: {str(e)}"}, status=status.HTTP_400_BAD_REQUEST)
        
        except ValidationError as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    @method_decorator(csrf_exempt, name="dispatch")
    def partial_update(self, request, pk=None) -> Response:
        """
        Update an existing message record.
        
        Args:
            request (Request): The request containing the updated message data.
            pk (int): The ID of the message to be updated.
            
        Returns:
            Response: The response with the status of the operation.
        """
        try:
            message_id = Message.objects.get(id=pk)
            data = json.loads(request.body)
            message_instance = self.message_service.get_by_id(message_id)
            self.message_service.update(data, message_instance)
            return Response("detail: The message was updated with success", status=status.HTTP_200_OK)
        except ValidationError as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"error": "An error occurred while updating messages."},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        

    @method_decorator(csrf_exempt, name="dispatch")
    def list(self, request) -> Response:
        """
        List all messages in the database.
        
        Args:
            request (Request): The request to fetch the list of messages.
            
        Returns:
            Response: The response containing the list of messages.
        """
        try:
            messages = self.message_service.get_all()
            serializer_class = self.get_serializer_class()
            serializer = serializer_class(messages, many=True)
            data_paginator = PaginatorConfig().paging_data(serializer.data)
            return Response(data_paginator, status=status.HTTP_200_OK)
        except ValidationError as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"error": "An error occurred while fetching messages."},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    @action(detail=False, methods=["get"], url_path=r"get_contact_id/(?P<contact>\d+)")
    @method_decorator(csrf_exempt, name="dispatch")
    def get_by_contact(self, request, contact: int) -> Response:
        """
        Retrieves messages for a specific contact.

        Args:
            request (Request): The HTTP request.
            contact (int): The ID of the contact whose messages should be retrieved.

        Returns:
            Response: A paginated response containing the messages for the contact.
        """
        try:
            messages = self.message_service.get_by_contact(contact)
            serializer_class = self.get_serializer_class()
            serializer = serializer_class(messages, many=True)
            data_paginator = PaginatorConfig().paging_data(serializer.data)
            return Response(data_paginator, status=status.HTTP_200_OK)
        except ValidationError as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"error": "An error occurred while fetching messages for the contact."},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    @action(detail=False, methods=["get"], url_path=r"get_support_agent_id/(?P<support_agent>\d+)")
    @method_decorator(csrf_exempt, name="dispatch")
    def get_by_support_agent(self, request, support_agent: int) -> Response:
        """
        Retrieves messages for a specific support agent.

        Args:
            request (Request): The HTTP request.
            support_agent (int): The ID of the support agent whose messages should be retrieved.

        Returns:
            Response: A paginated response containing the messages for the support agent.
        """
        try:
            messages = self.message_service.get_by_support_agent(support_agent)
            serializer_class = self.get_serializer_class()
            serializer = serializer_class(messages, many=True)
            data_paginator = PaginatorConfig().paging_data(serializer.data)
            return Response(data_paginator, status=status.HTTP_200_OK)
        except ValidationError as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"error": "An error occurred while fetching messages for the support agent."},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    @method_decorator(csrf_exempt, name="dispatch")
    def destroy(self, request, pk=None) -> Response:
        """
        Delete a message record by its ID.
        
        Args:
            request (Request): The request to delete the message.
            pk (int): The ID of the message to delete.
            
        Returns:
            Response: The response with the status of the operation.
        """
        try:
            self.message_service.delete(pk)
            return Response({"message_deleted": True}, status=status.HTTP_200_OK)
        
        except Message.DoesNotExist:
            return Response({"error": "Message not found."}, status=status.HTTP_404_NOT_FOUND)
        
        except ValidationError as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
