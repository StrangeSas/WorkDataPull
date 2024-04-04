import requests
from bs4 import BeautifulSoup
import fake_useragent
import time
import json

#https://www.youtube.com/watch?v=0_xwepyuV1E 6:53

def get_links(text):
    ua = fake_useragent.UserAgent()
    data = requests.get(
        url="https://krasnoyarsk.hh.ru/search/vacancy?L_save_area=true&text={text}&excluded_text=&area=113&salary=&currency_code=RUR&experience=doesNotMatter&order_by=relevance&search_period=0&items_on_page=50&page={page}",
        headers={"user-agent": ua.random}
    )
    soup = BeautifulSoup(data.content, 'lxml')
    try:
        page_count = int(soup.find("div", attrs={"class":"pager"}).find_all("span", recursive=False)[-1].find("a").find("span").text)
    except:
        return
    for page in range(page_count):
        try:
            data = requests.get(
                url="https://krasnoyarsk.hh.ru/search/vacancy?L_save_area=true&text={text}&excluded_text=&area=113&salary=&currency_code=RUR&experience=doesNotMatter&order_by=relevance&search_period=0&items_on_page=50&page={page}",
                headers={"user-agent": ua.random}
            )
            if data.status_code == 200:
                soup = BeautifulSoup(data.content, "lxml")
                for i in soup.find("div", attrs={"data-qa":"vacancy-serp__results"}).find_all("div", attrs={"class":"serp-item_link"}):
                    yield f'{i.find("a", "bloko-link").attrs["href"].split("?")[0]}'
        except Exception as e:
            print(f"{e}")
        time.sleep(1)
    print(page_count)
def get_resume(link):
    pass

if __name__ == "__main__":
   for a in get_links("BI-аналитик"):
       print(a)
"""
ua = fake_useragent.UserAgent()
data = requests.get(
    url="https://krasnoyarsk.hh.ru/search/vacancy?L_save_area=true&text={text}&excluded_text=&area=113&salary=&currency_code=RUR&experience=doesNotMatter&order_by=relevance&search_period=0&items_on_page=50&page={page}",
    headers={"user-agent": ua.random}
)
soup = BeautifulSoup(data.content, 'lxml')
print()

for i in soup.find("div", attrs={"data-qa":"vacancy-serp__results"}).find_all("div", attrs={"class":"serp-item_link"}):
    print(i.find("a", "bloko-link"))
    
    
    
    for i in soup.find("div", attrs={"data-qa":"vacancy-serp__results"}).find_all("div", attrs={"class":"serp-item_link"}):
                        print(i.find("a", "bloko-link"))
"""