from abc import ABC, abstractmethod

from message.models import Message

class AbstractMessageRepository(ABC):
    """
    Abstract base class for message repositories.
    Define the basic CRUD operations for handling messages.
    """

    @abstractmethod
    def create(data: dict) -> Message:
        """
        Create a new message record.
        
        Args:
            message_data (dict): The data for the message to be created.
        
        Raises:
            NotImplementedError: If the method is not implemented.
        """
        pass

    @abstractmethod
    def update(message: Message, message_data: dict) -> None:
        """
        Update an existing message record.
        
        Args:
            message_id (int): The ID of the message to be updated.
            message_data (dict): The updated data for the message.
        
        Raises:
            NotImplementedError: If the method is not implemented.
        """
        pass

    @abstractmethod
    def delete(message_id: int)-> None:
        """
        Delete a message record.
        
        Args:
            message_id (int): The ID of the message to be deleted.
        
        Raises:
            NotImplementedError: If the method is not implemented.
        """
        pass

    @abstractmethod
    def get_all()-> list[Message]:
        """
        Get all message records.
        
        Returns:
            list: A list of all messages.
        
        Raises:
            NotImplementedError: If the method is not implemented.
        """
        pass
