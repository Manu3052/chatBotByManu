from abc import ABC, abstractmethod
from typing import List

from message.models import Message

class AbstractMessageService(ABC):
    """
    Abstract class for defining methods related to message management.
    This class should be inherited by any concrete service class to implement message handling functionality.
    """

    @abstractmethod
    def create(self, data: dict) -> Message:
        """
        Method to create a new message.

        Args:
            data (dict): Data required to create a new message.

        Returns:
            Message: The created message instance.
        """
        pass

    @abstractmethod
    def update(self, data: dict, message: Message) -> None:
        """
        Method to update an existing message.

        Args:
            data (dict): Data to update the message.
            message (Message): The message instance to be updated.

        Returns:
            Message: The updated message instance.
        """
        pass
    
    @abstractmethod
    def get_by_id(self, message: int) -> Message:
        """
        Method to update an existing message.

        Args:
            message (int): Message Id

        Returns:
            Message: The updated message instance.
        """
        pass

    @abstractmethod
    def get_by_support_agent(self, support_agent: int) -> List['Message']:
        """
        Retrieves a list of records associated with a specific support agent.

        Args:
            request: The request object containing the current context information.
            support_agent (int): The ID of the support agent.

        Returns:
            List[SupportAgent]: A list of SupportAgent objects linked to the provided ID.
        """
        pass

    @abstractmethod
    def get_by_contact(self, contact: int) -> List['Message']:
        """
        Retrieves a list of records associated with a specific contact.

        Args:
            request: The request object containing the current context information.
            contact (int): The ID of the contact.

        Returns:
            List[Contact]: A list of Contact objects linked to the provided ID.
        """
        pass

    @abstractmethod
    def get_all(self) -> List[Message]:
        """
        Method to retrieve all messages.

        Returns:
            List[Message]: A list of all message instances.
        """
        pass
    @abstractmethod
    def delete(self, message_id: int) -> None:
        """
        Method to delete a message by its ID.

        Args:
            message_id (int): The unique identifier of the message to delete.
        """
        pass

