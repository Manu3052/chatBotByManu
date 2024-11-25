from abc import ABC, abstractmethod

from contact.models import Contact

class AbstractContactRepository(ABC):

    @abstractmethod
    def create(self, data: dict) -> Contact:
        pass

    @abstractmethod
    def update(self, data: dict, contact: Contact) -> None:
        """
        Method to update an existing contact.

        Args:
            data (dict): Data to update the contact.
            contact (Contact): The contact instance to be updated.

        Returns:
            Contact: The updated contact instance.
        """
        pass
    
    @abstractmethod
    def get_by_id(self, contact: int) -> Contact:
        """
        Method to update an existing contact.

        Args:
            contact (int): Contact Id

        Returns:
            Contact: The updated contact instance.
        """
        pass

    @abstractmethod
    def get_by_name(self, contact: int) -> Contact:
        """
        Method to update an existing contact.

        Args:
            contact (int): Contact Id

        Returns:
            Contact: The updated contact instance.
        """
        pass

    @abstractmethod
    def delete(self, Contact: int) -> None:
        """
        Method to delete a contact by its ID.

        Args:
            contact_id (int): The unique identifier of the contact to delete.
        """
        pass
