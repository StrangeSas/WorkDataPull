
import pandas as pd
import json
import sys
import numpy as np
from matplotlib import pyplot as plt
import matplotlib.cm as cm
import seaborn as sns
import spacy
from spacypdfreader.spacypdfreader import pdf_reader

special_character = '\n'

nlp_ger = spacy.load('/home/user/anaconda3/lib/python3.11/site-packages/de_core_news_sm/de_core_news_sm-3.7.0')

nlp_en = spacy.load('/home/user/anaconda3/lib/python3.11/site-packages/en_core_web_sm/en_core_web_sm-3.7.1')

with open ('files to parse/cdowiki-20240120-pages-articles-multistream-index.txt', 'r') as f:
    text = f.read()

doc = nlp_en(text)
list_of_sentences = [doc.text for sentences in doc.sents]

for i in doc.sents:
    print(i)