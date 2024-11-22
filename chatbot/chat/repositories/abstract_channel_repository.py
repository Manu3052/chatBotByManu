from abc import ABC, abstractmethod

from chat.models import Chat


class AbstractChannelRepository(ABC):
    """
    Abstract base class for a Channel Repository.

    Purpose:
        - Serves as a blueprint for repository implementations that handle 
          operations related to the Chat model.
        - Enforces a contract for implementing CRUD operations on Chat objects.

    Methods:
        - create(data: dict) -> Chat: Abstract method to create a new Chat instance.
        - update(data: dict) -> Chat: Abstract method to update an existing Chat instance.
        - delete(chat_id: int) -> Chat: Abstract method to delete a Chat instance by its ID.
        - get_all() -> Chat: Abstract method to retrieve all Chat instances.
    """

    @abstractmethod
    def create(self, data: dict) -> Chat:
        """
        Creates a new Chat instance.

        Args:
            - data (dict): A dictionary containing the chat data. Keys should match the Chat model's fields.

        Returns:
            - Chat: The created Chat instance.
        """
        pass
    
    @abstractmethod
    def update(self, data: dict) -> Chat:
        """
        Updates an existing Chat instance.

        Args:
            - data (dict): A dictionary with updated data for the chat.
            - chat (Chat): The Chat instance to be updated.

        Returns:
            - Chat: The updated Chat instance.
        """
        pass

    @abstractmethod
    def delete(self, chat_id: int) -> Chat:
        """
        Deletes a Chat instance.

        Args:
            - chat_id (int): The unique identifier of the Chat to delete.

        Returns:
            - None
        """
        pass

    @abstractmethod
    def get_all(self) -> Chat:
        """
        Retrieves all Chat instances.

        Returns:
            - QuerySet: A QuerySet of all Chat instances.
        """
        pass
