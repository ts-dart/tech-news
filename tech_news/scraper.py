import re
import requests
from time import sleep
from parsel import Selector


def fetch(url):
    try:
        response = requests.get(url, timeout=1)
        sleep(1)

        return response.text if response.status_code == 200 else None
    except requests.exceptions.ReadTimeout:
        return None


def scrape_novidades(html_content):
    selector = Selector(text=html_content)
    return selector.css('a.cs-overlay-link ::attr(href)').getall()


def scrape_next_page_link(html_content):
    selector = Selector(text=html_content)
    return selector.css('a.next ::attr(href)').get()


def scrape_noticia(html_content):
    selector = Selector(text=html_content)
    title = selector.css('h1.entry-title ::text').get()

    news = {
        'url': get_url(title, selector.css('link ::attr(href)').getall()),
        'title': selector.css('h1.entry-title ::text').get(),
        'writer': selector.css('span.author a ::text').get(),
        'summary': (
            re.sub('<.*?>', '', selector.css('p').get()).replace(u'\xa0', u'')
        ),
        'comments_count': len(selector.css('ol.comment-list li').getall()),
        'timestamp': selector.css('li.meta-date ::text').get(),
        'tags': selector.css('section.post-tags li a ::text').getall(),
        'category': selector.css('span.label ::text').get(),
    }

    ''' print('-----------------')
    print(news)
    print('-----------------')
    print(news['summary']) '''
    return news


def get_url():
    ...

    # selector.css('link ::attr(href)').getall()[3][:-len('amp/')]

# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
