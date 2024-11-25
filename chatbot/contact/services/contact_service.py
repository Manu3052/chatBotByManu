from django.forms import ValidationError
from contact.repositories.contact_repository import ContactRepository
from contact.models import Contact
from rest_framework import status
from contact.services.abstract_contact_service import AbstractContactService


class ContactService(AbstractContactService):
    """
    Concrete implementation of the AbstractContactService for managing Contact records.
    This class interacts with the ContactRepository to perform CRUD operations on the `Contact` model.
    """

    def __init__(self, contact_repository: ContactRepository = ContactRepository()):
        """
        Initializes the ContactService with the provided ContactRepository.
        
        Args:
            contact_repository (ContactRepository, optional): The repository used to interact with the Contact model.
        """
        self.contact_repository = contact_repository

    def create(self, data: dict) -> Contact:
        """
        Creates a new contact using the provided data.

        Args:
            data (dict): A dictionary containing the data to create the new contact.
                         Should include 'name', 'email', 'cpf', 'telephone', etc.

        Returns:
            Contact: The newly created contact object.
        """
        contact = self.contact_repository.create(data)
        if not isinstance(contact, Contact):
            raise ValidationError(detail="An error occurred while creating a contact.", status=status.HTTP_400_BAD_REQUEST)
        return contact

    def update(self, contact: Contact, data: dict) -> Contact:
        """
        Updates an existing contact with the provided data.

        Args:
            contact (Contact): The contact instance to be updated.
            data (dict): A dictionary containing the data to update the contact.

        Returns:
            Contact: The updated contact instance.
        """
        self.contact_repository.update(contact, data)
        return contact

    def get_contact_by_id(self, contact_id: int) -> Contact:
        """
        Retrieves a contact by its unique ID.

        Args:
            contact_id (int): The ID of the contact to retrieve.

        Returns:
            Contact: The contact object corresponding to the provided ID.
        """
        contact = self.contact_repository.get_by_id(contact_id)
        if not isinstance(contact, Contact):
            raise ValidationError(detail="There is no contact with this ID", status=status.HTTP_404_NOT_FOUND)
        return contact

    def get_contact_by_name(self, name: str) -> Contact:
        """
        Retrieves a contact by its name.

        Args:
            name (str): The name of the contact to retrieve.

        Returns:
            Contact: The contact object corresponding to the provided name.
        """
        contact = self.contact_repository.get_by_name(name)
        if not isinstance(contact, Contact):
            raise ValidationError(detail="There is no contact with this Name", status=status.HTTP_404_NOT_FOUND)
        return contact
    
    def get_contact_by_name_intern(self, name: str) -> Contact:
        """
        Retrieves a contact by its name and returns None

        Args:
            name (str): The name of the contact to retrieve.

        Returns:
            Contact: The contact object corresponding to the provided name.
        """
        contact = self.contact_repository.get_by_name(name)
        if not isinstance(contact, Contact):
            return None
        return contact

    def delete(self, contact_id: int) -> None:
        """
        Deletes a contact by its ID.

        Args:
            contact_id (int): The unique identifier of the contact to delete.
        """
        self.contact_repository.delete(contact_id)

    def get_all_contacts(self) -> list[Contact]:
        """
        Retrieves all contact records from the database.

        Returns:
            list[Contact]: A list of all Contact objects.
        """
        contacts = self.contact_repository.get_all()
        if len(contacts) < 0:
            raise ValidationError(detail="There are no contacts.", status=status.HTTP_404_NOT_FOUND)
        return contacts
