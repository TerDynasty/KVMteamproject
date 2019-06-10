import telebot
import requests
import time
from telebot import types
bot = telebot.TeleBot('883226012:AAHkIxPBq2maVp9EQHLIpuDr8n60Pthbbq4')


@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = types.ReplyKeyboardMarkup(True)
    markup.add('Games', 'Business', 'Sports', 'Total news', 'Music', 'Fashion')
    msg = bot.send_message(message.chat.id, 'Choose the topic: ', reply_markup=markup)
    bot.register_next_step_handler(msg, reply_func)


@bot.message_handler(commands=['text'])
def reply_func(message):
    if message.text == 'Games' or 'Sports' or 'Business' or 'Total news' or 'Music' or 'Fashion':
        msg = process_response(message.text, message)
        bot.register_next_step_handler(msg, reply_func)
    else:
        bot.send_message(message.chat.id, "I can't understand you, choose one of the topics or type /start")


def process_response(topic, message):
    token = '8b9f58ea8b9f58ea8b9f58eab98bf5a2d188b9f8b9f58ead767545b404b0c2293ca5e22'
    version = '5.95'
    domain_list = []
    current_time = time.time()
    all_posts = []
    most_likes1, most_likes2, most_likes3 = 0, 0, 0
    most_liked1_index, most_liked2_index, most_liked3_index = 0, 0, 0
    with open('file_domain.txt', 'r') as f:
        for row in f:
            parts = row.split(';')
            if parts[0] == topic:
                for n in range(1, len(parts)):
                    domain_list.append(parts[n])
    for domain in domain_list:
        response = requests.get('https://api.vk.com/method/wall.get',
                                params={
                                    'access_token': token,
                                    'v': version,
                                    'domain': domain,
                                    'count': 100
                                }
                                )
        data = response.json()['response']['items']
        all_posts.extend(data)
        for i in range(100):
            if all_posts[i]['likes']['count'] > most_likes1 and all_posts[i]['date'] >= current_time - 86400:
                most_likes3 = most_likes2
                most_liked3_index = most_liked2_index
                most_likes2 = most_likes1
                most_liked2_index = most_liked1_index
                most_likes1 = all_posts[i]['likes']['count']
                most_liked1_index = i
            elif all_posts[i]['likes']['count'] > most_likes2 and all_posts[i]['date'] >= current_time - 86400:
                most_likes3 = most_likes2
                most_liked3_index = most_liked2_index
                most_likes2 = all_posts[i]['likes']['count']
                most_liked2_index = i
            elif all_posts[i]['likes']['count'] > most_likes3 and all_posts[i]['date'] >= current_time - 86400:
                most_likes3 = all_posts[i]['likes']['count']
                most_liked3_index = i
        for index in [most_liked1_index, most_liked2_index, most_liked3_index]:
            photo_url = ''
            links = ''
            for attachment in all_posts[index]['attachments']:
                if attachment['type'] == 'photo':
                    photo_url = attachment['photo']['sizes'][-1]['url']
                elif attachment['type'] == 'link':
                    links = attachment['link']['url']
            if photo_url:
                if links:
                    msg = bot.send_photo(message.chat.id, photo_url,
                                         f'{all_posts[index]["text"]}, More detailed: {links[0]}')
                else:
                    msg = bot.send_photo(message.chat.id, photo_url, f'{all_posts[index]["text"]}')
            else:
                msg = bot.send_message(message.chat.id, f'{all_posts[index]["text"]}')
    return msg


bot.polling(none_stop=True, interval=0)
