from dataclasses import dataclass
from typing import List
from django.contrib.contenttypes.models import ContentType

from contact.models import Contact
from message.models import Message
from message.repositories.abstract_message_repository import AbstractMessageRepository
from supportAgent.models import SupportAgent


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
    def get_by_contact(contact: int) -> List['Message']:
        """
        Retrieves all messages sent by a specific contact.

        Args:
            contact (int): The ID of the contact whose messages should be retrieved.

        Returns:
            List[Message]: A list of messages sent by the contact.
        """
        contact_instance = Contact.objects.get(id=contact)
        contact_content_type = ContentType.objects.get_for_model(contact_instance)
        messages = Message.objects.filter(
            sender_content_type=contact_content_type,
            sender_object_id=contact_instance.id
        ).values()
        return messages

    @staticmethod
    def get_by_support_agent(support_agent: int) -> List['Message']:
        """
        Retrieves all messages sent by a specific support agent.

        Args:
            support_agent (int): The ID of the support agent whose messages should be retrieved.

        Returns:
            List[Message]: A list of messages sent by the support agent.
        """
        support_agent_instance = SupportAgent.objects.get(id=support_agent)        
        support_agent_content_type = ContentType.objects.get_for_model(support_agent_instance)
        messages = Message.objects.filter(
            sender_content_type=support_agent_content_type,
            sender_object_id=support_agent_instance.id
        )
        return messages

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
