# Requisito 1
import requests
import time

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
            return response.text
    except requests.ReadTimeout:
        return None


# Requisito 2
def scrape_updates(html_content):
    """Seu código deve vir aqui"""


# Requisito 3
def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""


# Requisito 4
def scrape_news(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""


# if __name__ == '__main__':
#     res = fetch(BASE_URL)
#     print(res)
