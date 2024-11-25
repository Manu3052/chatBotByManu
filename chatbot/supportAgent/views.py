from dataclasses import dataclass
from rest_framework.exceptions import ValidationError
from supportAgent.repositories.support_agent_repository import SupportAgentRepository

@dataclass
class SupportAgentService:
    support_agent_repository: SupportAgentRepository

    def __init__(self, support_agent_repository: SupportAgentRepository):
        """
        Inicializa o serviço de SupportAgent com o repositório fornecido.

        Args:
            support_agent_repository (SupportAgentRepository): Instância do repositório de agentes de suporte.
        """
        self.support_agent_repository = support_agent_repository

    def create(self, data: dict):
        """
        Cria um novo agente de suporte com base nos dados fornecidos.

        Args:
            data (dict): Dados necessários para criar o agente de suporte.

        Returns:
            SupportAgent: A instância do agente criado.
        """
        return self.support_agent_repository.create(data)

    def get_by_id(self, agent_id: int):
        """
        Recupera um agente de suporte pelo ID.

        Args:
            agent_id (int): ID do agente de suporte.

        Returns:
            SupportAgent: A instância do agente encontrado.
        """
        return self.support_agent_repository.get_by_id(agent_id)
