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

    news = {
        'url': get_url(selector.css('link ::attr(href)').getall()),
        'title': (
            selector.css('h1.entry-title ::text').get()
            .replace(u'\xa0', u'').strip()
        ),
        'writer': selector.css('span.author a ::text').get(),
        'summary': (
            re.sub('<.*?>', '', selector.css('p').get())
            .replace(u'\xa0', u'').strip()
        ),
        'comments_count': len(selector.css('ol.comment-list li').getall()),
        'timestamp': selector.css('li.meta-date ::text').get(),
        'tags': selector.css('section.post-tags li a ::text').getall(),
        'category': selector.css('span.label ::text').get(),
    }

    return news


def get_url(href_list):
    for href in href_list:
        if 'blog.betrybe.com' in href:
            return href


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
