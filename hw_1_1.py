"""
task_1_1
Посмотреть документацию к API GitHub, разобраться как вывести список репозиториев
для конкретного пользователя, сохранить JSON-вывод в файле *.json.
"""

import requests
import json


def get_query_to_files(url, user):
    my_query = requests.get(f'{url}/users/{user}/repos').json()
    with open('query_data.json', 'w') as write_to_json:
        json.dump(my_query, write_to_json)
    return my_query


def get_repos():
    list_repos = get_query_to_files(url, user)
    for elem in list_repos:
        print(elem['name'])
    print(f'Всего {len(list_repos)} репозиториев')


if __name__ == '__main__':
    url = 'https://api.github.com'
    user = 'AndyMcMagadan'

    get_repos()
