import datetime
from typing import List, Tuple
from tech_news.database import search_news


# Requisito 7
def search_by_title(title: str) -> List[Tuple[str, str]]:
    query = {"title": {"$regex": title, "$options": "i"}}
    result = search_news(query)

    titles_and_urls_by_title = []
    for news in result:
        titles_and_urls_by_title.append((news["title"], news["url"]))
    return titles_and_urls_by_title


# Requisito 8
def search_by_date(date: str) -> List[Tuple[str, str]]:
    try:
        parsed_date = datetime.datetime.strptime(date, "%Y-%m-%d")
        formatted_date = parsed_date.strftime("%d/%m/%Y")
    except ValueError:
        raise ValueError("Data inválida")

    query = {"timestamp": formatted_date}
    result = search_news(query)

    titles_and_urls_by_date = []
    for news in result:
        titles_and_urls_by_date.append((news["title"], news["url"]))

    return titles_and_urls_by_date


# Requisito 9
def search_by_category(category: str) -> List[Tuple[str, str]]:
    query = {"category": {"$regex": category, "$options": "i"}}
    print(query)
    result = search_news(query)

    titles_and_urls_by_category = []
    for news in result:
        titles_and_urls_by_category.append((news["title"], news["url"]))

    return titles_and_urls_by_category


# if __name__ == '__main__':
#     result_title = search_by_title('Cabos de rede')
#     result_date = search_by_date('2023-04-05')
#     result_category = search_by_category('Desenvolvimento Web')
#     print(result_title)
#     print(result_date)
#     print(result_category)
