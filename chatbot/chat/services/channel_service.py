from dataclasses import dataclass

from rest_framework.exceptions import ValidationError

from chat.models import Chat
from chat.repositories.channel_repository import ChannelRepository
from chat.services.abstract_channel_service import AbstractChannelService


@dataclass
class ChannelService(AbstractChannelService):
    """
    Serviço responsável pela gestão de canais (Chats), implementando métodos 
    para criar, atualizar, deletar e recuperar informações de canais.

    Esta classe utiliza um repositório de canal para realizar operações no banco de dados.
    """
    
    channel_repository = ChannelRepository()

    def create(self, data: dict) -> Chat:
        """
        Cria um novo canal (Chat) com base nos dados fornecidos.

        Args:
            data (dict): Dados necessários para criar o chat.

        Returns:
            Chat: A instância do chat criado.
        """
        return self.channel_repository.create(data)
    
    def update(self, data: dict, chat: Chat) -> None:
        """
        Atualiza as informações de um canal (Chat) existente.

        Args:
            data (dict): Dados para atualizar o chat.
            chat (Chat): A instância do chat a ser atualizada.

        Returns:
            None
        """
        return self.channel_repository.update(data, chat)

    def delete(self, chat_id: int) -> None:
        """
        Remove um canal (Chat) com base no seu identificador único.

        Args:
            chat_id (int): Identificador único do chat a ser excluído.

        Returns:
            None
        """
        return self.channel_repository.delete(chat_id)

    def get_all(self) -> list[Chat]:
        """
        Recupera todos os canais (Chats) existentes.

        Returns:
            list[Chat]: Uma lista contendo todas as instâncias de chat.
        """
        return self.channel_repository.get_all()
