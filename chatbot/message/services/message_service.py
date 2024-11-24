from dataclasses import dataclass
from typing import List, Union

from rest_framework.exceptions import ValidationError

from contact.models import Contact
from message.models import Message
from message.repositories.message_repository import MessageRepository
from message.services.abstract_message_service import AbstractMessageService
from rest_framework import status
from supportAgent.models import SupportAgent


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
    
    def get_by_support_agent(self, support_agent: int) -> List['Message']:
        """
        Retrieves messages associated with a specific support agent.

        Args:
            support_agent (int): The ID of the support agent.

        Returns:
            List[SupportAgent]: A list of messages related to the specified support agent.

        Raises:
            ValidationError: If no messages are found for the given support agent, with a 404 HTTP status.
        """
        messages = self.message_repository.get_by_support_agent(support_agent)
        if len(messages) == 0:
            raise ValidationError(
                detail="Messages from support agents were not found.",
                code=status.HTTP_404_NOT_FOUND
            )
        return messages

    def get_by_contact(self, contact: int) -> List['Message']:
        """
        Retrieves messages associated with a specific contact.

        Args:
            contact (int): The ID of the contact.

        Returns:
            List[Contact]: A list of messages related to the specified contact.

        Raises:
            ValidationError: If no messages are found for the given contact, with a 404 HTTP status.
        """
        messages = self.message_repository.get_by_contact(contact)
        if len(messages) == 0:
            raise ValidationError(
                detail="Messages from contacts were not found.",
                code=status.HTTP_404_NOT_FOUND
            )
        return messages

    def get_all(self) -> List[Message]:
        """
        Method to retrieve all messages.
        
        Returns:
            List[Message]: A list of all message instances.
        """
        messages = self.message_repository.get_all()
        if len(messages) == 0:
            raise ValidationError(detail="Messages were not found.", code=status.HTTP_404_NOT_FOUND)
        return messages

    def delete(self, message_id: int) -> None:
        """
        Method to delete a message by its ID.
        
        Args:
            message_id (int): The unique identifier of the message to delete.
        
        Raises:
            ValidationError: If the message cannot be deleted.
        """
        self.message_repository.delete(message_id)


