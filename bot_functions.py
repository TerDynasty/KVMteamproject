import requests

import TelegramBotAPI

token = '8b9f58ea8b9f58ea8b9f58eab98bf5a2d188b9f8b9f58ead767545b404b0c2293ca5e22'
version = '5.95'
domain_name = 'dlyanxs'

#https://api.vk.com/method/wall.get?access_token=token&v=5.95&domain=domain_name

#def get_api(url)


def read_file(file_name, topic):
    domain_list = []
    with open(file_name, 'r') as f:
        for i in range(3):
            line = f.readline()
            parts = line.split(';')
            if parts[0] == topic:
                for i in range(1, len(parts)):
                    domain_list.append(parts[i])
    return domain_list


def get_response(domain_name, token, version):
    response = requests.get('https://api.vk.com/method/wall.get',
                         params={
                             'access_token': token,
                             'v': version,
                             'domain': domain_name
                         }
                         )
    return response


def process_response(token, version, topic):
    domain_list = read_file('file_domain.csv', topic)
    for i in domain_list:
        response = get_response(i, token, version)
        data = response.json()






data = read_file('file_domain.csv', 'Economics')
print(data)
