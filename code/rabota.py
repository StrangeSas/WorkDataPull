import requests
from bs4 import BeautifulSoup
import fake_useragent
import time
import json

#https://www.youtube.com/watch?v=0_xwepyuV1E 6:53

"""
По сути, мне сейчас узко направленный скрипт на hh.ru - следует обобщить,
Либо сделать отдельные скрипты для разных сайтов и уже между ними переключаться
Я думаю в данном случае будет лучше исполнить именно многопроцессорность запросов.

Сделать скрипты для напила всех заявок с разных сайтов.
Сделать скрипт, что будет запускать всех их и обрабатывать нужные данные

Потом полученные json обрабатывать в csv формат.

"""

def get_links(text):
    ua = fake_useragent.UserAgent()
    data = requests.get(
        url="https://krasnoyarsk.hh.ru/search/vacancy?L_save_area=true&text={text}&excluded_text=&salary=&currency_code=RUR&experience=doesNotMatter&order_by=relevance&search_period=0&items_on_page=50&page={page}",
        headers={"user-agent": ua.ff}
    )
    soup = BeautifulSoup(data.content, 'lxml')
    try:
        page_count = int(soup.find("div", attrs={"class":"pager"}).find_all("span", recursive=False)[-1].find("a").find("span").text)
    except:
        return
    for page in range(page_count):
        try:
            data = requests.get(
                url="https://krasnoyarsk.hh.ru/search/vacancy?L_save_area=true&text={text}&excluded_text=&salary=&currency_code=RUR&experience=doesNotMatter&order_by=relevance&search_period=0&items_on_page=50&page={page}",
                headers={"user-agent": ua.random}
            )
            if data.status_code == 200:
                soup = BeautifulSoup(data.content, "lxml")
                for i in soup.find("div", attrs={"data-qa":"vacancy-serp__results"}).find_all("div", attrs={"class":"serp-item"}):
                    yield f'{i.find("a", "bloko-link").attrs["href"].split("?")[0]}'
        except Exception as e:
            print(f"{e}")
        time.sleep(0.1)
    print(page_count)
def get_resume(link):
    ua = fake_useragent.UserAgent()
    data = requests.get(
        url=link,
        headers={"user-agent": ua.random}
    )
    if data.status_code != 200:
        return
    soup = BeautifulSoup(data.content, "lxml")
    try:
        name = soup.find(attrs={"class":"resume-block__title-text"}).text
    except:
        name =""
    try:
        salary = soup.find(attrs={"class":"resume-block__salary"}).text.replace("\u2009","").replace("\xa0", " ")
    except:
        salary =""
    try:
        tags = [tag.text for tag in soup.find(attrs={"class":"bloko-tag-list"}).find_all(attrs={"span":"bloko-tag__section_text"})]
    except:
        tags =[]
    resume = {
        "name":name,
        "salary":salary,
        "link":link,
        "tags": tags
    }
    return resume

if __name__ == "__main__":
    data = []
    for a in get_links("BI-аналитик"):
        data.append(get_resume(a))
        time.sleep(0.1)
        with open("data.json","w",encoding="utf-8") as f:
            json.dump(data,f,indent=4,ensure_ascii=False)