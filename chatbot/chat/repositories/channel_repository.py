from chat.models import Chat
from chat.repositories.abstract_channel_repository import \
    AbstractChannelRepository


class ChannelRepository(AbstractChannelRepository):
    """
    Concrete implementation of the AbstractChannelRepository for managing Chat instances.

    Methods:
        - create(data: dict) -> Chat: Creates a new Chat instance with the provided data.
        - update(data: dict, chat: Chat) -> Chat: Updates an existing Chat instance with the given data.
        - delete(chat_id: int): Deletes a Chat instance identified by its ID.
        - get_all() -> QuerySet: Retrieves all Chat instances.
    """

    @staticmethod
    def create(data: dict) -> Chat:
        """
        Creates a new Chat instance.

        Args:
            - data (dict): A dictionary containing the chat data. Keys should match the Chat model's fields.

        Returns:
            - Chat: The created Chat instance.
        """
        data_copy = data
        if 'support_agent_id' in data:
            support_agent_id = data_copy.pop("support_agent_id")
        if 'contact_id' in data:
            contact_id = data_copy.pop("contact_id")
        chat = Chat.objects.create(**data_copy)
        if 'support_agent_id' in data:
            chat.support_agent_id.set(support_agent_id[0])
        if 'contact_id' in data:
            chat.contact_id.set(contact_id[0])
        chat.save()
        return chat
    
    @staticmethod
    def update(data: dict, chat: Chat) -> Chat:
        """
        Updates an existing Chat instance.

        Args:
            - data (dict): A dictionary with updated data for the chat.
            - chat (Chat): The Chat instance to be updated.

        Returns:
            - Chat: The updated Chat instance.
        """
        support_agent = data.pop("support_agent_id")
        for key, value in data.item():
            setattr(chat, key, value)
        chat.support_agent_id.set(support_agent[0])
        chat.save()
    
    @staticmethod
    def delete(chat_id: int) -> Chat:
        """
        Deletes a Chat instance.

        Args:
            - chat_id (int): The unique identifier of the Chat to delete.

        Returns:
            - None
        """
        Chat.objects.filter(id=chat_id).delete()

    @staticmethod
    def get_all() -> Chat:
        """
        Retrieves all Chat instances.

        Returns:
            - QuerySet: A QuerySet of all Chat instances.
        """
        chats = Chat.objects.all()
        return chats

