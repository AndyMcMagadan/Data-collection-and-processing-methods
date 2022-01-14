"""
task_3_2
Написать функцию, которая производит поиск и выводит на экран вакансии
с заработной платой больше введённой суммы (необходимо анализировать оба поля зарплаты).
"""

from pymongo import MongoClient
from pprint import pprint


def find_and_compare(salary):
    vac_cont = 0
    for vac in vacancy.find({'$or': [{'salary_to': {'$gte': salary}}, {'salary_from': {'$gte': salary}}]}):
        pprint(vac)
        vac_cont += 1
    if vac_cont == 0:
        print('Нет вакансий с требуемой заработной платой.')


if __name__ == '__main__':
    client = MongoClient('127.0.0.1', 27017)
    db = client['vacancy1401']
    vacancy = db.vacancy

    my_salary = int(input('Введите желаемую заработную плату в рублях: '))
    find_and_compare(my_salary)
