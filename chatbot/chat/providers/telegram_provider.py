
import telebot

from chat.providers.abstract_provider_config import AbstractProviderConfig

TELEGRAM_API_KEY = "7914621325:AAG4Pl9ckiK7i3HhHzXUFq1Jzef9ZRBJQxI"

bot = telebot.TeleBot(TELEGRAM_API_KEY)
class TelegramProvider(AbstractProviderConfig):
        
    @bot.message_handler(commands=["ola"])
    def reply(self, message):
        bot.reply_to(message, "Olá aqui")


