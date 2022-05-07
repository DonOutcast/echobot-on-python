import telebot
import config

bot = telebot.TeleBot(config.TOKEN)

@bot.message_handler(commands=["start"])
def welcom(message):
    bot.send_message(message.chat.id, "Добро пожаловать")


@bot.message_handler(content_types=["text"])
def povotr(message):
    bot.send_message(message.chat.id, message.text)

bot.polling(none_stop=True)


