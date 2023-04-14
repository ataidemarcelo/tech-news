import requests
import time
from bs4 import BeautifulSoup

BASE_URL = 'https://blog.betrybe.com/'

HEADERS = {"user-agent": "Fake user-agent"}


# Requisito 1
def fetch(url):
    try:
        response = requests.get(
            BASE_URL,
            headers=HEADERS,
            timeout=3
        )
        time.sleep(1)

        if response.status_code == 200:
            html_content = response.text
            return html_content
    except requests.ReadTimeout:
        return None


# Requisito 2
def scrape_updates(html_content):
    soup = BeautifulSoup(html_content, "html.parser")
    news_list = soup.find_all("article", {"class": "entry-preview"})
    list_links_to_news_pages = []
    for news in news_list:
        link = news.find("a")["href"]
        list_links_to_news_pages.append(link)

    return list_links_to_news_pages


# Requisito 3
def scrape_next_page_link(html_content):
    soup = BeautifulSoup(html_content, "html.parser")
    next_page_link_element = soup.find("a", {"class": "next"})
    if next_page_link_element:
        next_page_link = next_page_link_element["href"]
        return next_page_link
    return None


# Requisito 4
def scrape_news(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""


# if __name__ == '__main__':
#     html_content = fetch(BASE_URL)
#     link = scrape_next_page_link(html_content)
#     print(link)
