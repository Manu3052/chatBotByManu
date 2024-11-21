from abc import ABC, abstractmethod


class AbstractChannelService(ABC):

    @abstractmethod
    def reply(self, data: dict):
        pass

    @abstractmethod
    def get_bot(self, bot_name):
        pass