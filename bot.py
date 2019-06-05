import telebot
bot = telebot.TeleBot('883226012:AAHkIxPBq2maVp9EQHLIpuDr8n60Pthbbq4')


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == "Hi":
        bot.send_message(message.from_user.id, "Hi, I am HottestNewsBot and now I'm in the development stage")
    elif message.text == "/help":
        bot.send_message(message.from_user.id, "Type Hi")
    else:
        bot.send_message(message.from_user.id, "I can't understand you, type /help.")


bot.polling(none_stop=True, interval=0)
