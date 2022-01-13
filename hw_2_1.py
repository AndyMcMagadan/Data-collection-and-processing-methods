import requests

page_number = 0
search_str = "qlik"
area_str = "1"

# Адрес api метода для GET - запроса и параметры
url = 'https://api.hh.ru/vacancies'
param = {
    "text": search_str,
    "area": area_str,
    "page": page_number
}

# Отправляем get request (GET - запрос)
response = requests.get(url, param)
data = response.json()

# Создаем пустой List (данные) с заголовками и счетчик для страниц
list_data = [['id vacancy', 'name vacancy', 'area name', 'salary from', 'salary to', 'currency']]
dict_number = 0

# Определяем количество страниц и проходим их в цикле
for i in range(0, data['pages']):
    param_cycle = {
        "text": search_str,
        "area": area_str,
        "page": i
    }

    response_cycle = requests.get(url, param_cycle)
    print(f'Страница № {(i + 1)} сайта {url}')

    result = dict(response_cycle.json())
    result = result['items']
    # Парсим исходный list формата Json в список данных
    for y in range(0, len(result) - 1):
        id = result[y]['id']
        name = result[y]['name']
        area = result[y]['area']['name']
        salary = result[y]['salary']
        # разделяем заработную плату по параметрам "от", "до", "валюта", если указаны
        if salary:
            salary_from = salary['from']
            if salary_from:
                salary_from = float(salary_from)
            salary_to = salary['to']
            if salary_to:
                salary_to = float(salary_to)
            currency = salary['currency']
        else:
            salary_from = None
            salary_to = ''
            currency = ''
        list_data.append([id, name, area, salary_from, salary_to, currency])
        print(list_data[dict_number])
        dict_number += 1

    print("=" * 80)

