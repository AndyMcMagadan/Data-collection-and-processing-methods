"""
task_4
Написать приложение, которое собирает основные новости с сайта на выбор news.mail.ru, lenta.ru,
yandex-новости. Для парсинга использовать XPath. Структура данных должна содержать:
1. название источника;
2. наименование новости;
3. ссылку на новость;
4. дата публикации.
Сложить собранные новости в БД
Минимум один сайт, максимум - все три
"""

from datetime import date
from lxml import html
import requests
from pprint import pprint
from pymongo import MongoClient
from pymongo.errors import DuplicateKeyError


def news_parsing(dom, url, day):
    items = dom.xpath("//a[contains(@class, '_longgrid')]")
    news = []
    for item in items:
        new = {}
        title = item.xpath(".//span[@class='card-mini__title']/text()")
        for el in title:
            if el:
                title = el
        link = url + item.xpath("./@href")[0][1:]
        news_date = item.xpath(".//time[@class='card-mini__date']/text()")
        for el in news_date:
            if el:
                news_date = f'{day} {el}'

        if title:
            new['_id'] = int(abs(hash(link)))
            new['source'] = url
            new['title'] = title
            new['link'] = link
            new['date'] = news_date
        news.append(new)
    return news


def insert_news_to_database(new):
    try:
        news.insert_one(new)
    except DuplicateKeyError:
        pass


if __name__ == '__main__':
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/97.0.4692.71 Safari/537.36'}
    url = 'https://lenta.ru/'
    response = requests.get(url, headers=header)
    my_dom = html.fromstring(response.text)
    today = str(date.today())
    print(today, type(today))

    client = MongoClient('127.0.0.1', 27017)
    db = client['news1801']
    news = db.news1801

    result = news_parsing(my_dom, url, today)

    for new in result:
        if new:
            insert_news_to_database(new)
            pprint(new)
