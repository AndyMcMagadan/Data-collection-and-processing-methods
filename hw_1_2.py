"""
task_1_2
Изучить список открытых API (https://www.programmableweb.com/category/all/apis).
Найти среди них любое, требующее авторизацию (любого типа). Выполнить запросы к нему,
пройдя авторизацию. Ответ сервера записать в файл.
"""

import requests
import json


def get_query_to_files(url, headers):
    my_query = requests.get(url=url, headers=headers)
    with open('data.json', 'w') as new_file:
        json.dump(my_query.json(), new_file)
    print(my_query)


if __name__ == '__main__':
    my_url = 'https://api.oilpriceapi.com/v1/prices/latest'
    my_headers = {
        'Authorization': 'Token 65c394d8ba27cad1bdcc781667e1d3d8',
        'Content-Type': 'application/json',
    }

    get_query_to_files(my_url, my_headers)
