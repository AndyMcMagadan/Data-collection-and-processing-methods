"""
task_3_1
Развернуть у себя на компьютере/виртуальной машине/хостинге MongoDB и реализовать функцию,
которая будет добавлять только новые вакансии/продукты в вашу базу.
"""

import requests
from pymongo import MongoClient
from pprint import pprint
from pymongo.errors import DuplicateKeyError


# Отправляем get request (GET - запрос)
def get_response(url, param):
    response = requests.get(url, param)
    data = response.json()
    return data


def separate_salary(salary):
    # разделяем заработную плату по параметрам "от", "до", "валюта", если указаны
    if not salary:
        salary_from = None
        salary_to = None
        currency = None
    else:
        salary_from = salary['from']
        if salary_from:
            salary_from = float(salary_from)
        salary_to = salary['to']
        if salary_to:
            salary_to = float(salary_to)
        currency = salary['currency']
    return [salary_from, salary_to, currency]


def add_new_vacations(search_str, area_str, data):
    # Счетчик новых вакансий
    new_vacancy_counter = 0
    # Определяем количество страниц и проходим их в цикле
    for i in range(0, data['pages']):
        url = 'https://api.hh.ru/vacancies'
        param_cycle = {
            "text": search_str,
            "area": area_str,
            "page": i
        }

        response_cycle = get_response(url, param_cycle)
        print(f'Страница № {(i + 1)} сайта {url}')

        result = dict(response_cycle)
        result = result['items']
        # Парсим исходный list формата Json в dictionary (словарь данных)
        for y in range(0, len(result) - 1):
            doc_salary = result[y]['salary']
            data_doc = {
                '_id': result[y]['id'],
                'name': result[y]['name'],
                'area_name': result[y]['area']['name'],
                'salary_from': separate_salary(doc_salary)[0],
                'salary_to': separate_salary(doc_salary)[1],
                'currency': separate_salary(doc_salary)[2]
            }
            try:
                vacancy.insert_one(data_doc)
                new_vacancy_counter += 1
            except DuplicateKeyError:
                pass
            # Очищаем словать данных для следующей записи
            pprint(data_doc)
            data_doc.clear()

        print("=" * 80)

    print(f'Добавлено {new_vacancy_counter} новых вакансий.')


if __name__ == '__main__':
    my_search_str = "qlik"
    my_area_str = "1"
    page_number = 0

    # Адрес api метода для GET - запроса и параметры
    my_url = 'https://api.hh.ru/vacancies'
    my_param = {
        "text": my_search_str,
        "area": my_area_str,
        "page": page_number
    }

    client = MongoClient('127.0.0.1', 27017)
    db = client['vacancy1401']
    vacancy = db.vacancy

    data_response = get_response(my_url, my_param)
    add_new_vacations(my_search_str, my_area_str, data_response)
