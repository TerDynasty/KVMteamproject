import requests


def process_response(topic):
    token = '8b9f58ea8b9f58ea8b9f58eab98bf5a2d188b9f8b9f58ead767545b404b0c2293ca5e22'
    version = '5.95'
    domain_list = []
    with open('file_domain.csv', 'r') as f:
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
        data = response.json()['response']['item']

