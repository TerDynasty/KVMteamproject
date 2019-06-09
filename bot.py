import telebot
from telebot import types
bot = telebot.TeleBot('883226012:AAHkIxPBq2maVp9EQHLIpuDr8n60Pthbbq4')


@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = types.ReplyKeyboardMarkup(True)
    markup.add('Games', 'Business', 'Sport', 'Total news')
    msg = bot.send_message(message.chat.id, 'Choose the topic: ', reply_markup=markup)
    bot.register_next_step_handler(msg, reply_func)


@bot.message_handler(commands=['text'])
def reply_func(message):
    if message.text == 'Games':
        msg = bot.send_message(message.chat.id, "Hi, I am HottestNewsBot and now I'm in the development stage")
        bot.register_next_step_handler(msg, reply_func)
    elif message.text == 'Business':
        msg = bot.send_message(message.chat.id, "Hi, I am HottestNewsBot and now I'm in the development stage")
        bot.register_next_step_handler(msg, reply_func)
    elif message.text == 'Sport':
        msg = bot.send_message(message.chat.id, "Hi, I am HottestNewsBot and now I'm in the development stage")
        bot.register_next_step_handler(msg, reply_func)
    elif message.text == 'Total news':
        msg = bot.send_message(message.chat.id, "Hi, I am HottestNewsBot and now I'm in the development stage")
        bot.register_next_step_handler(msg, reply_func)
    else:
        bot.send_message(message.chat.id, "I can't understand you, choose one of the topics or type /start")


bot.polling(none_stop=True, interval=0)
