import requests
import time


def process_response(topic):
    token = '8b9f58ea8b9f58ea8b9f58eab98bf5a2d188b9f8b9f58ead767545b404b0c2293ca5e22'
    version = '5.95'
    domain_list = []
    current_time = time.time()
    all_posts = []
    most_liked1, most_liked2, most_liked3 = 0, 0, 0
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
            if all_posts[i]['likes']['count'] > most_liked1 and all_posts[i]['date'] >= current_time - 86400:
                most_liked3 = most_liked2
                most_liked3_index = most_liked2_index
                most_liked2 = most_liked1
                most_liked2_index = most_liked1_index
                most_liked1 = all_posts
                most_liked1_index = i
            elif all_posts[i]['likes']['count'] > most_liked2 and all_posts[i]['date'] >= current_time - 86400:
                most_liked3 = most_liked2
                most_liked3_index = most_liked2_index
                most_liked2 = most_liked1
                most_liked2_index = i
            elif all_posts[i]['likes']['count'] > most_liked3 and all_posts[i]['date'] >= current_time - 86400:
                most_liked3 = all_posts[i]
                most_liked3_index = i


