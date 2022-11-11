from datetime import datetime
from tech_news.database import search_news


def search_by_title(title):
    news_list = search_news({})
    news_found = []

    for news in news_list:
        if title.lower() in news['title']:
            news_found.append((news['title'], news['url']))

    return news_found


def search_by_date(date):
    try:
        news_list = search_news({})
        date_arr = date.split('-')
        formated_date = f'{date_arr[2]}/{date_arr[1]}/{date_arr[0]}'
        datetime.strptime(formated_date, '%d/%m/%Y')
        news_found = []

        for news in news_list:
            if formated_date == news['timestamp']:
                news_found.append((news['title'], news['url']))

        return news_found
    except (ValueError, IndexError):
        raise ValueError('Data inválida')


def search_by_tag(tag):
    news_list = search_news({})
    news_found = []

    for news in news_list:
        for tg in news['tags']:
            if tag.lower() == tg.lower():
                news_found.append((news['title'], news['url']))

    return news_found


def search_by_category(category):
    news_list = search_news({})
    news_found = []

    for news in news_list:
        if category.lower() == news['category'].lower():
            news_found.append((news['title'], news['url']))

    return news_found
