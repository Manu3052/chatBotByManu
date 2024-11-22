import json

from django.views.decorators.csrf import csrf_exempt
from rest_framework import permissions, status
from rest_framework.decorators import action
from django.utils.decorators import method_decorator
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from message.models import Message
from message.serializers.message_create_serializer import \
    MessageCreateSerializer
from message.serializers.message_create_serializer import MessageCreateSerializer
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
            message = Message.objects.get(id=pk)
            data = json.loads(request.body)
            updated_message = self.message_service.update(data, message)
            serializer = MessageCreateSerializer(updated_message)
            
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        except Message.DoesNotExist:
            return Response({"error": "Message not found."}, status=status.HTTP_404_NOT_FOUND)
        
        except (json.JSONDecodeError, KeyError) as e:
            return Response({"error": f"Invalid data format: {str(e)}"}, status=status.HTTP_400_BAD_REQUEST)
        
        except ValidationError as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    @method_decorator(csrf_exempt, name="dispatch")
    def list(self, request) -> Response:
        """
        List all messages in the database.
        
        Args:
            request (Request): The request to fetch the list of messages.
            
        Returns:
            Response: The response containing the list of messages.
        """
        messages = self.message_service.get_all()
        serializer = MessageCreateSerializer(messages, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

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
