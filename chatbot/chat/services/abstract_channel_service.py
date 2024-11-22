from abc import ABC, abstractmethod

from chat.models import Chat


class AbstractChannelService(ABC):
    """
    Abstract class for defining the interface of a Channel Service.
    
    This class ensures that all subclasses implement the necessary methods 
    for managing channel-related operations.
    """

    @abstractmethod
    def create(self, data: dict) -> Chat:
        """
        Abstract method to create a new chat.
        
        Args:
            data (dict): Data required to create a new chat.

        Returns:
            Chat: The created chat instance.
        """
        pass

    @abstractmethod
    def update(self, data: dict, chat: Chat) -> None:
        """
        Abstract method to update an existing chat.
        
        Args:
            data (dict): Data to update the chat.
            chat (Chat): The chat instance to be updated.
        """
        pass

    @abstractmethod
    def delete(self, chat_id: int) -> None:
        """
        Abstract method to delete a chat by its ID.
        
        Args:
            chat_id (int): The unique identifier of the chat to delete.
        """
        pass

    @abstractmethod
    def get_all(self) -> list[Chat]:
        """
        Abstract method to retrieve all chats.
        
        Returns:
            list[Chat]: A list of all chat instances.
        """
        pass
