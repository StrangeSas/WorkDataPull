import requests
from bs4 import BeautifulSoup
import fake_useragent
import time
import json

#https://www.youtube.com/watch?v=0_xwepyuV1E 6:53

"""
Найти заявки с авито и приколы с тэгами с него

Вспомнился прикол с созданием системы, по взбиранию всего информационного следа о пользователе
благодаря которому машина потом берёт место человека, продолжая его деятельность, будто ничего
не изменилось.

Хм... Мне нужно потыкать с тем, как сделать торовское шифрование исходящего трафика
"""

def get_links(text):
    ua = fake_useragent.UserAgent()
    data = requests.get(

        url="https://www.avito.ru/all/vakansii?p={page}&q={text}",
        headers={"user-agent": ua.ff}
    )
    soup = BeautifulSoup(data.content, 'lxml')
    try:
        page_count = int(soup.find("div", attrs={"class":"pagination-pages clearfix"}).find_all("a", recursive=False)[-1].attrs["href"].split("=")[-1].text)
    except:
        page_count = 1
    for page in range(page_count):
        try:
            data = requests.get(
                url="https://www.avito.ru/all/vakansii?p={page}&q={text}",
                headers={"user-agent": ua.random}
            )
            if data.status_code == 200:
                soup = BeautifulSoup(data.content, "lxml")
                for i in soup.find("div", attrs={"class":"items-items-kAJAg"}).find_all("div", attrs={"data-marker":"item"}):
                    #Находятся все ссылки в блоке, после чего они все приписываются в лист. Из него
                    #берётся первая ссылка, что ссылат на работу, а не на компанию
                    yield f'https://www.avito.ru{i.find_all("a", attrs={"itemprop":"url"})[0].attrs["href"].split("?")[0]}'
        except Exception as e:
            print(f"{e}")
        time.sleep(0.2)
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
        name = soup.find_all("h1",attrs={"class":"styles-module-root-TWVK"})[0].text
    except:
        name =""
    try:
        salary = soup.find(attrs={"itemprop":"price"}).text.replace("\u2009","").replace("&nbps;", " ")
    except:
        salary =""
    try:
        exp = soup.find_all("ul", attrs={"class":"params-paramsList-_awNW"})[-1].text.replace("\u2009","").replace("\xa0", " ")
    except:
        exp = []
    resume = {
        "name":name,
        "salary":salary,
        "link":link,
        "exp": exp
    }
    return resume

def put_in_json_av(stra):
    if __name__ == "__main__":
        data = []
        for a in get_links(stra):
            data.append(get_resume(a))
            time.sleep(0.1)
            with open("data.json","w",encoding="utf-8") as f:
                json.dump(data,f,indent=4,ensure_ascii=False)


