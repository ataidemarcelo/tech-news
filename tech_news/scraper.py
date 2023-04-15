import requests
import time
from bs4 import BeautifulSoup
from tech_news.database import create_news

BASE_URL = 'https://blog.betrybe.com/'

HEADERS = {"user-agent": "Fake user-agent"}


# Requisito 1
def fetch(url):
    try:
        response = requests.get(
            url,
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
    soup = BeautifulSoup(html_content, "html.parser")
    reading_time_text = soup.find("li", {"class": "meta-reading-time"}).text
    reading_time = int(reading_time_text.split()[0])

    return {
        "url": soup.find("link", {"rel": "canonical"})["href"],
        "title": soup.find("h1", {"class": "entry-title"}).text.rstrip(),
        "timestamp": soup.find("li", {"class": "meta-date"}).text,
        "writer": soup.find("span", {"class": "author"}).text,
        "reading_time": reading_time,
        "summary": soup.find("p").text.rstrip(),
        "category": soup.find("span", {"class": "label"}).text,
    }


# Requisito 5
def get_tech_news(amount):
    html_content = fetch(BASE_URL)
    list_links_to_news_pages = scrape_updates(html_content)
    next_page_link = scrape_next_page_link(html_content)
    news_dict_list = []

    all_links_to_new_page = []
    all_links_to_new_page.extend(list_links_to_news_pages)

    while amount > len(all_links_to_new_page):
        html_content = fetch(next_page_link)
        list_links_to_news_pages = scrape_updates(html_content)

        all_links_to_new_page.extend(list_links_to_news_pages)
        next_page_link = scrape_next_page_link(html_content)

    for index in range(amount):
        html_content = fetch(all_links_to_new_page[index])
        news_dict = scrape_news(html_content)
        news_dict_list.append(news_dict)

    create_news(news_dict_list)

    return news_dict_list


# if __name__ == '__main__':
#     html_content = fetch(BASE_URL)
#     list_links_to_news_pages = scrape_updates(html_content)
#     next_page_link = scrape_next_page_link(html_content)
#     news_dict_list = []

#     amount = 30
#     all_links_to_new_page = []
#     all_links_to_new_page.extend(list_links_to_news_pages)

#     while amount > len(all_links_to_new_page):
#         html_content = fetch(next_page_link)
#         list_links_to_news_pages = scrape_updates(html_content)

#         all_links_to_new_page.extend(list_links_to_news_pages)
#         next_page_link = scrape_next_page_link(html_content)
#     print(len(all_links_to_new_page))
#     for index in range(amount):
#         html_content = fetch(all_links_to_new_page[index])
#         news = scrape_news(html_content)
#         news_dict_list.append(news)

#     create_news(news_dict_list)
