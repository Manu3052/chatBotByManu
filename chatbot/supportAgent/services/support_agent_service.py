from dataclasses import dataclass

from rest_framework.exceptions import ValidationError

from supportAgent.repositories.support_agent_repository import SupportAgentRepository



@dataclass
class SupportAgentService:
    
    support_agent_repository = SupportAgentRepository()

    def create(self, data: dict):
        """
        Cria um novo canal (Chat) com base nos dados fornecidos.

        Args:
            data (dict): Dados necessários para criar o chat.

        Returns:
            Chat: A instância do chat criado.
        """
        return self.support_agent_repository.create(data)
    


    def get_by_id(self, chat_id: int):
        """
        Recupera todos os canais (Chats) existentes.

        Returns:
            list[Chat]: Uma lista contendo todas as instâncias de support_agent.
        """
        return self.support_agent_repository.get_all()

    def get_by_chat_id(self, chat_id: int):
        support_agent = self.support_agent_repository.get_by_id(chat_id)
        if support_agent:
            raise ValidationError(detail="There is no support_agent with this id")
        return support_agent
