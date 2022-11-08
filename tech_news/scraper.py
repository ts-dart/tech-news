import requests
from time import sleep


def fetch(url):
    try:
        response = requests.get(url, timeout=1)
        sleep(1)

        return response.text if response.status_code == 200 else None
    except requests.exceptions.ReadTimeout:
        return None


# Requisito 2
def scrape_novidades(html_content):
    """Seu código deve vir aqui"""


# Requisito 3
def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""


# Requisito 4
def scrape_noticia(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
