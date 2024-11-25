import json
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from rest_framework import permissions, status
from rest_framework.decorators import action
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from contact.models import Contact  
from contact.serializers.contact_create_serializer import ContactCreateSerializer
from contact.serializers.contact_list_serializer import ContactListSerializer 
from contact.services.contact_service import ContactService
from message.utils.pagination import PaginatorConfig 

class ContactViewSet(ModelViewSet):
    """
    ViewSet for managing contacts.

    This ViewSet provides operations to create, update, list, and delete contact records. 
    Additionally, it supports filtering contacts by specific attributes.

    Methods:
        create: Creates a new contact record.
        list: Lists all contact records in the database.
        partial_update: Partially updates a contact record by its ID.
        destroy: Deletes a contact record by its ID.
        get_by_attribute: Retrieves contacts filtered by a specific attribute.

    Attributes:
        permission_classes: Defines the access permissions for the ViewSet. 
                            Here, it allows access to any user.
        serializer_class: The default serializer class used by the ViewSet.
        queryset: The default queryset for retrieving all `Contact` records.
        pagination_class: Specifies the pagination configuration used for paginated responses.
    """

    permission_classes = [permissions.AllowAny]
    serializer_class = ContactListSerializer
    queryset = Contact.objects.all()
    pagination_class = PaginatorConfig

    def get_serializer_class(self):
        """
        Determines the appropriate serializer class based on the action being performed.

        Returns:
            The serializer class for the current action.
        """
        if self.action == "create":
            return ContactCreateSerializer
        elif self.action == "list":
            return ContactListSerializer
        elif self.action in ["get_by_attribute", "get_by_agent"]:
            return ContactListSerializer

        return ContactListSerializer

    def __init__(self, contact_service: ContactService = ContactService(), **kwargs):
        """
        Initializes the ViewSet with the contact service.

        Args:
            contact_service (ContactService, optional): Service used to handle contact operations.
        """
        super().__init__(**kwargs)
        self.contact_service = contact_service

    @method_decorator(csrf_exempt, name="dispatch")
    def create(self, request) -> Response:
        """
        Creates a new contact record.

        Args:
            request (Request): The request containing contact data.

        Returns:
            Response: A response indicating the success or failure of the operation.
        """
        try:
            data = json.loads(request.body)
            self.contact_service.create(data)
            return Response({"contact_created": True}, status=status.HTTP_201_CREATED)
        except (json.JSONDecodeError, KeyError) as e:
            return Response({"error": f"Invalid data format: {str(e)}"}, status=status.HTTP_400_BAD_REQUEST)
        except ValidationError as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    @method_decorator(csrf_exempt, name="dispatch")
    def partial_update(self, request, pk=None) -> Response:
        """
        Partially updates a contact record by its ID.

        Args:
            request (Request): The request containing update data.
            pk (int): The ID of the contact to update.

        Returns:
            Response: A response indicating the success or failure of the operation.
        """
        try:
            contact_instance = self.contact_service.get_contact_by_id(pk)
            data = json.loads(request.body)
            self.contact_service.update(data, contact_instance)
            return Response("detail: The contact was updated successfully", status=status.HTTP_200_OK)
        except ValidationError as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"error": "An error occurred while updating the contact."},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    @method_decorator(csrf_exempt, name="dispatch")
    def list(self, request) -> Response:
        """
        Lists all contact records.

        Args:
            request (Request): The request to list contacts.

        Returns:
            Response: A response containing the list of contacts with pagination.
        """
        try:
            contacts = self.contact_service.get_all_contacts()
            serializer_class = self.get_serializer_class()
            serializer = serializer_class(contacts, many=True)
            data_paginator = PaginatorConfig().paging_data(serializer.data)
            return Response(data_paginator, status=status.HTTP_200_OK)
        except ValidationError as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"error": "An error occurred while fetching contacts."},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    @method_decorator(csrf_exempt, name="dispatch")
    def destroy(self, request, pk=None) -> Response:
        """
        Deletes a contact record by its ID.

        Args:
            request (Request): The request to delete the contact.
            pk (int): The ID of the contact to delete.

        Returns:
            Response: A response indicating the success or failure of the operation.
        """
        try:
            self.contact_service.delete(pk)
            return Response({"contact_deleted": True}, status=status.HTTP_200_OK)
        except Contact.DoesNotExist:
            return Response({"error": "Contact not found."}, status=status.HTTP_404_NOT_FOUND)
        except ValidationError as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=["get"], url_path=r"get_by_name/(?P<name>.+)")
    @method_decorator(csrf_exempt, name="dispatch")
    def get_by_name(self, request, name: str) -> Response:
        """
        Retrieves contacts filtered by a specific name.

        Args:
            request (Request): The HTTP request.
            name (str): The name used for filtering contacts.

        Returns:
            Response: A response containing the filtered contacts.
        """
        try:
            contacts = self.contact_service.get_contact_by_name(name)
            serializer_class = self.get_serializer_class()
            serializer = serializer_class(contacts, many=True)
            data_paginator = PaginatorConfig().paging_data(serializer.data)
            return Response(data_paginator, status=status.HTTP_200_OK)
        except ValidationError as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"error": "An error occurred while filtering contacts."},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)

