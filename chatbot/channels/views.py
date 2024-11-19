import telebot

TELEGRAM_API_KEY = "7914621325:AAG4Pl9ckiK7i3HhHzXUFq1Jzef9ZRBJQxI"

bot = telebot.TeleBot(TELEGRAM_API_KEY)

@bot.message_handler(commands=["ola"])
def responder(mensagem):
    print(mensagem)
    bot.reply_to(mensagem, "Olá aqui")

bot.polling()

# class ChannelViewSet(ModelViewSet):