import telebot
from telebot import types
bot = telebot.TeleBot('883226012:AAHkIxPBq2maVp9EQHLIpuDr8n60Pthbbq4')


@bot.message(content_types=['text'])
def direction_choice(message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(*[types.KeyboardButton(name) for name in ['Games', 'Business', 'Sport', 'Total news']])
    msg = bot.send_message(message.chat.id, 'Choose the topic', reply_markup=keyboard)
    bot.register_next_step_handler(msg, name)


def name(message):
    if message.text == 'Games':
        bot.send_message(message.from_user.id, "Hi, I am HottestNewsBot and now I'm in the development stage")
    elif message.text == 'Business':
        bot.send_message(message.from_user.id, "Hi, I am HottestNewsBot and now I'm in the development stage")
    elif message.text == 'Sport':
        bot.send_message(message.from_user.id, "Hi, I am HottestNewsBot and now I'm in the development stage")
    elif message.text == 'Total news':
        bot.send_message(message.from_user.id, "Hi, I am HottestNewsBot and now I'm in the development stage")
    else:
        bot.send_message(message.from_user.id, "I can't understand you, choose one of the topics.")


bot.polling(none_stop=True, interval=0)
