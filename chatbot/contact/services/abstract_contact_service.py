from abc import ABC, abstractmethod
from contact.models import Contact

class AbstractContactService(ABC):
    """
    Abstract class defining the methods for interacting with the `Contact` model.
    This abstraction allows for creating, updating, retrieving, and deleting contacts.
    """

    @abstractmethod
    def create(self, data: dict) -> Contact:
        """
        Create a new contact based on provided data.

        Args:
            data (dict): The data used to create the new contact. The dictionary should
                         contain attributes like 'name', 'email', 'cpf', etc.

        Returns:
            Contact: The newly created contact object.
        """
        pass

    @abstractmethod
    def update(self, contact: Contact, data: dict) -> Contact:
        """
        Update an existing contact with the provided data.

        Args:
            contact (Contact): The contact instance to be updated.
            data (dict): A dictionary containing the data to update the contact.

        Returns:
            Contact: The updated contact instance.
        """
        pass

    @abstractmethod
    def get_contact_by_name_intern(self, name: str) -> Contact:
        """
        Retrieves a contact by its name and returns None

        Args:
            name (str): The name of the contact to retrieve.

        Returns:
            Contact: The contact object corresponding to the provided name.
        """

    @abstractmethod
    def get_contact_by_id(self, contact_id: int) -> Contact:
        """
        Retrieve a contact by its unique ID.

        Args:
            contact_id (int): The ID of the contact to retrieve.

        Returns:
            Contact: The contact object corresponding to the provided ID.
        """
        pass

    @abstractmethod
    def get_contact_by_name(self, name: str) -> Contact:
        """
        Retrieve a contact by its name.

        Args:
            name (str): The name of the contact to retrieve.

        Returns:
            Contact: The contact object corresponding to the provided name.
        """
        pass

    @abstractmethod
    def delete(self, contact_id: int) -> None:
        """
        Delete a contact by its ID.

        Args:
            contact_id (int): The unique identifier of the contact to delete.
        """
        pass

    @abstractmethod
    def get_all_contacts(self) -> list[Contact]:
        """
        Retrieve all contact records.

        Returns:
            list[Contact]: A list of all contact objects.
        """
        pass
