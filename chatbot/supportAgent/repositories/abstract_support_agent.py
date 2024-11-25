from abc import ABC, abstractmethod

from chat.models import Chat
from supportAgent.models import SupportAgent


class AbstractSupportAgentRepository(ABC):
    """
    Abstract base class for a SupportAgent Repository.

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
    def create(self, data: dict) -> SupportAgent:
        """
        Creates a new SupportAgent instance.

        Args:
            - data (dict): A dictionary containing the SupportAgent data. Keys should match the SupportAgent model's fields.

        Returns:
            - SupportAgent: The created SupportAgent instance.
        """
        pass
    

    @abstractmethod
    def get_by_id(self, support_id: int) -> SupportAgent:
        """
        Retrieves all SupportAgent instances.

        Returns:
            - QuerySet: A QuerySet of all SupportAgent instances.
        """
        pass
