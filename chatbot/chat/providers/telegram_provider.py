
import os

from telebot import TeleBot
from telebot.types import Chat, Message, User
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

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
        message = message["message"]
        chat_data = message['chat']
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

    def verify_existing_message(self, message:str) -> bool:
        return True

    def create_keyboard(self, buttons):
        keyboard = InlineKeyboardMarkup()
        for text, callback_data in buttons:
            keyboard.add(InlineKeyboardButton(text, callback_data=callback_data))
        return keyboard

    def setup_handlers(self, data: dict, message: str = 'callback'):
        """
        Sets up the command and message handlers for the bot.
        """
        if "start" in message.lower():
            message_telegram = self.transform_data_to_message(data)
            self.handle_start(message_telegram)
        elif 'callback_query' in data:
            self.handle_query(data)

    def handle_start(self, message: Message):
        """
        Sends a welcome message and a keyboard with options when the user interacts via '/start' or 'start'.

        Args:
            message (Message): The incoming Telegram message object.
        """
        welcome_text = (
            "Olá! Antes de continuar, posso perguntar se você já utiliza algum dos produtos da Weni? "
            "Isso vai me ajudar a oferecer as informações mais relevantes para você. 😊"
        )
        buttons = [
            ("Sim, já utilizo produtos Weni", "use_weni"),
            ("Não, ainda não utilizo produtos Weni", "dont_use_weni")
        ]
        BOT.send_message(message.chat.id, welcome_text, reply_markup=self.create_keyboard(buttons))


    @BOT.callback_query_handler(func=lambda call: True)
    def handle_query(self, call: dict):
        answer = call['callback_query']['data']
        message_id = call['callback_query']['message']['message_id']
        chat_id = call['callback_query']['from']['id']
        if answer == "use_weni":
            text = (
                "Que ótimo saber que você já utiliza produtos da Weni! 😊\n\n"
                "Como posso te ajudar a tirar o máximo proveito da plataforma? Gostaria de saber mais sobre recursos específicos "
                "como o WeniGPT, BotBuilder ou Weni Chats? Ou há algo mais que você precisa de suporte? Estou aqui para ajudar! 🚀"
            )
            buttons = [
                ("Preciso de suporte para algum produto Weni", "support_weni"),
                ("Quero adquirir novos produtos Weni", "new_products_weni")
            ]
            BOT.edit_message_text(text, chat_id, message_id, reply_markup=self.create_keyboard(buttons))
        
        elif answer == "dont_use_weni":
            text = (
                "Caso ainda não utilize produtos Weni, posso te ajudar a conhecer nossas soluções e como elas podem beneficiar sua empresa. "
                "Aqui estão algumas opções:"
            )
            buttons = [
                ("Gostaria de saber mais sobre os produtos Weni", "product_details"),
                ("Gostaria de contratar os serviços/Falar com especialista", "hire_services")
            ]
            BOT.edit_message_text(text, chat_id, message_id, reply_markup=self.create_keyboard(buttons))
        
        elif answer == "support_weni":
            text = "Vou transferir você para o suporte agora. 😊\n\nPor favor, descreva qual é o problema que você está enfrentando e com qual produto Weni."
            BOT.edit_message_text(text, chat_id, message_id)
        
        elif answer == "new_products_weni":
            text = (
                "Claro! Para ajudá-lo com novos produtos da Weni, você pode escolher entre:\n\n"
                "1️⃣ Receber explicações sobre nossos produtos (como WeniGPT, BotBuilder e Weni Chats)\n"
                "2️⃣ Falar com um especialista para uma orientação personalizada"
            )
            buttons = [
                ("Receber explicações sobre produtos", "product_details"),
                ("Falar com um especialista", "talk_specialist"),
            ]
            BOT.edit_message_text(text, chat_id, message_id, reply_markup=self.create_keyboard(buttons))

        elif answer == "product_details":
            text = (
                """
                    Vamos conhecer cada um dos nossos produtos? 🚀

                    Weni IA
                    Com a Weni IA, você transforma o atendimento da sua empresa! Nossa tecnologia própria permite criar agentes inteligentes que oferecem respostas rápidas, atendimentos mais humanos e até mesmo automatizam vendas. Quer elevar a satisfação dos seus clientes? Essa é a solução ideal!

                    BotBuilder Intuitivo
                    Se você gosta de ter controle total, vai adorar o nosso BotBuilder! Ele é um módulo no-code que te permite criar fluxos personalizados do zero. Com os módulos Flows e Studio, você constrói e gerencia chatbots poderosos sem complicação.

                    Canais & Integrações Weni
                    Precisa conectar suas ferramentas favoritas? Com o módulo Integrations, é fácil! Ele te permite integrar nossa plataforma às principais ferramentas do mercado, como WhatsApp, CRMs e muito mais, tudo em apenas alguns cliques. Assim, você centraliza suas operações e otimiza o dia a dia.

                    Atendimentos que fluem com Weni Chats
                    Chegou a hora de melhorar o atendimento humano! O Weni Chats é o módulo ideal para gerenciar contatos e conversas em um único espaço integrado e intuitivo. Atenda seus clientes pelo WhatsApp e outros canais em uma plataforma personalizada e eficiente. Tudo o que você precisa para oferecer um suporte ágil e eficaz.
                """
            )
            buttons = [
                ("Falar com um especialista", "talk_specialist"),
            ]
            BOT.edit_message_text(text, chat_id, message_id, reply_markup=self.create_keyboard(buttons))

        elif answer == "hire_services":
            text = "Entendido! Vou conectar você com um especialista para te ajudar a contratar nossos serviços. 😊"
            BOT.edit_message_text(text, chat_id, message_id)
        

    def verify_commands(self):
        """
        Verifies and processes any bot commands.

        This method can be extended to handle specific Telegram commands
        by overriding the parent method.
        """
        return super().verify_commands()

    @BOT.message_handler()
    def reply(self, message: Message, supportMessage: str):
        BOT.send_message(message, supportMessage)


