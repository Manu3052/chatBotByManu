
import os

from telebot import TeleBot
from telebot.types import Chat, Message, User

from chat.providers.abstract_provider_config import AbstractProviderConfig

BOT = TeleBot(os.environ.get('TELEGRAM_API_KEY'))
class TelegramProvider(AbstractProviderConfig):
    """
    TelegramProvider class handles interactions with the Telegram Bot API.

    This class implements methods to transform incoming data from Telegram into structured objects 
    and to send responses back via the Telegram Bot.

    Methods:
        - transform_data_to_message(message: dict) -> Message: Converts raw incoming Telegram data into a `Message` object.
        - verify_commands(): Verifies and executes bot commands (overrides method from AbstractProviderConfig).
        - reply(message: Message, supportMessage: str): Sends a reply to a given Telegram message.

    Attributes:
        - BOT: Instance of the TeleBot initialized with the Telegram API key.
    """
    def transform_data_to_message(self, message: dict) -> Message:
        """
        Transforms raw Telegram message data into a `Message` object.

        Args:
            message (dict): The raw message data received from Telegram.

        Returns:
            Message: A structured Message object containing information about the chat and user.
        """
        chat_data = message["chat"]
        chat = Chat(
            id=chat_data["id"],
            type=chat_data["type"],
            title=chat_data.get("title"),
            username=chat_data.get("username"),
            first_name=chat_data.get("first_name"),
            last_name=chat_data.get("last_name")
        )
        
        user_data = message["from"]
        user = User(
            id=user_data["id"],
            is_bot=user_data["is_bot"],
            first_name=user_data.get("first_name"),
            last_name=user_data.get("last_name"),
            username=user_data.get("username"),
            language_code=user_data.get("language_code")
        )
        
        message_obj = Message(
            message_id=message["message_id"],
            date=message["date"],
            chat=chat,
            from_user=user,
            content_type="text",
            options={},
            json_string=None
        )
        return message_obj

    def verify_commands(self):
        """
        Verifies and processes any bot commands.

        This method can be extended to handle specific Telegram commands
        by overriding the parent method.
        """
        return super().verify_commands()

    @BOT.message_handler()
    def reply(self, message: Message, supportMessage: str):
        BOT.reply_to(message, supportMessage)


