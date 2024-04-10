"""
import json
import csv
import pandas as pd

with open('data.json', encoding='utf-8') as f:
    df = pd.read_json(f)

df.to_csv('csvfile.csv', encoding='utf-8', index=False)

print(df.head())
"""
import requests
from bs4 import BeautifulSoup
import fake_useragent
import time
import json
import concurrent.futures

ua = fake_useragent.UserAgent()
data = requests.get(
    url="https://krasnoyarsk.hh.ru/vacancy/96389515",
    headers={"user-agent": ua.random}
)

soup = BeautifulSoup(data.content, "lxml")
region = soup.find("p", attrs={"class":"vacancy-creation-time-redesigned"}).text.replace("\u2009","").replace("\xa0", " ").split(" ")
print(region[-1])