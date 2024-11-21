
from channels.config.abstract_bot_config import AbstractBotConfig
from typing import Union
from channels.providers.telegram_provider import TelegramProvider
from channels.services.abstract_channel_service import AbstractChannelService


class ChannelService(AbstractChannelService):

    def __init__(self) -> None:
        self.bots ={"telegram": TelegramProvider()}

    def reply(self, data: dict):
        bot = self.get_bot(bot_name=data.get('bot_name'))
        bot.reply(data.get('message'))

    def get_bot(self, bot_name) -> Union[TelegramProvider]:
        if bot_name in self.bots:
            return self.bots[bot_name]
        else:
            raise Exception("Bot does not exist")