from abc import ABC, abstractmethod

from chat.models import Chat
from supportAgent.models import SupportAgent
from supportAgent.repositories.abstract_support_agent import AbstractSupportAgentRepository



class SupportAgentRepository(AbstractSupportAgentRepository):
    """
    Abstract base class for a SupportAgent Repository.

    Purpose:
        - Serves as a blueprint for repository implementations that handle 
          operations related to the support_agent model.
        - Enforces a contract for implementing CRUD operations on support_agent objects.

    Methods:
        - create(data: dict) -> support_agent: Abstract method to create a new support_agent instance.
        - get_by_id() -> support_agent: Abstract method to retrieve all support_agent instances.
    """

    @abstractmethod
    def create(self, data: dict) -> SupportAgent:
        """
        Creates a new support_agent instance.

        Args:
            - data (dict): A dictionary containing the support_agent data. Keys should match the support_agent model's fields.

        Returns:
            - support_agent: The created support_agent instance.
        """
        support_agent = support_agent.objects.create(**data)
        support_agent.save()
        return support_agent
    

    @abstractmethod
    def get_by_id(self, support_id: int) -> SupportAgent:
        """
        Retrieves all support_agent instances.

        Returns:
            - QuerySet: A QuerySet of all support_agent instances.
        """
        support_agent = support_agent.objects.filter(support_agent=support_id).first()
        return support_agent