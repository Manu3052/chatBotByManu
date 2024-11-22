from dataclasses import dataclass

from message.models import Message
from message.repositories.abstract_message_repository import AbstractMessageRepository


@dataclass
class MessageRepository(AbstractMessageRepository):
    """
    Concrete implementation of the AbstractMessageRepository class for managing Message records.
    
    This repository provides CRUD operations (Create, Update, Delete, and Get) for messages.
    The methods interact with the Django ORM to perform operations on the 'Message' model.
    """
    
    @staticmethod
    def create(data: dict) -> Message:
        """
        Creates a new message record in the database.
        
        Args:
            data (dict): A dictionary containing the data for the new message. The dictionary
                         should include message attributes and the associated chat information.
                         
        Returns:
            Message: The created Message object.
        
        Raises:
            ValueError: If the data provided is invalid or incomplete.
        """
        message = Message.objects.create(**data)
        message.save()
        return message

    @staticmethod
    def update(message: Message, message_data: dict) -> None:
        """
        Updates an existing message record with the provided data.
        
        Args:
            message (Message): The Message object to be updated.
            message_data (dict): A dictionary containing the new data for the message.
            
        Raises:
            ValueError: If the data provided is invalid or incomplete.
        """
        chat = message_data.pop("chat")
        for key, value in message_data.items():
            setattr(message, key, value)
        message.chat.set(chat[0])
        message.save()

    @staticmethod
    def delete(message_id: int) -> None:
        """
        Deletes the message record with the given ID.
        
        Args:
            message_id (int): The ID of the message to be deleted.
        
        Raises:
            DoesNotExist: If no message with the given ID exists.
        """
        Message.objects.filter(id=message_id).delete()

    @staticmethod
    def get_all() -> list[Message]:
        """
        Retrieves all message records from the database.
        
        Returns:
            list[Message]: A list of all Message objects.
        """
        messages = Message.objects.all()
        return messages
