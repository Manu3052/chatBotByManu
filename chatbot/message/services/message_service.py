from dataclasses import dataclass
from typing import List, Union

from rest_framework.exceptions import ValidationError

from message.models import Message
from message.repositories.message_repository import MessageRepository
from message.services.abstract_message_service import AbstractMessageService


@dataclass
class MessageService(AbstractMessageService):
    """
    Service class responsible for managing messages. This service includes methods
    to create, update, list, and delete messages.
    """
    
    message_repository = AbstractMessageRepository = MessageRepository()  

    def create(self, data: dict) -> Message:
        """
        Method to create a new message.
        
        Args:
            data (dict): Data required to create a new message.

        Returns:
            Message: The created message instance.
        
        """
        message = self.message_repository.create(data)
        return message

    def update(self, data: dict, message: Message) -> None:
        """
        Method to update an existing message.
        
        Args:
            data (dict): Data to update the message.
            message (Message): The message instance to be updated.
        
        Returns:
            Message: The updated message instance.
        
        """
        updated_message = self.message_repository.update(data, message)
        return updated_message

    def delete(self, message_id: int) -> None:
        """
        Method to delete a message by its ID.
        
        Args:
            message_id (int): The unique identifier of the message to delete.
        
        Raises:
            ValidationError: If the message cannot be deleted.
        """
        self.message_repository.delete(message_id)


    def get_all(self) -> List[Message]:
        """
        Method to retrieve all messages.
        
        Returns:
            List[Message]: A list of all message instances.
        """
        messages = self.message_repository.get_all()
        return messages

