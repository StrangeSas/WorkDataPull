
import urllib.request
from bs4 import BeautifulSoup
from translate import Translator
import spacy
import pandas as pd



nlp_ru = spacy.load('/home/user/anaconda3/lib/python3.11/site-packages/ru_core_news_sm/ru_core_news_sm-3.7.0')
nlp_en = spacy.load('/home/user/anaconda3/lib/python3.11/site-packages/en_core_web_sm/en_core_web_sm-3.7.1')
translator = Translator(from_lang="en", to_lang="ru")

user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'
url = "https://stackoverflow.com/questions/328356/extracting-text-from-html-file-using-python"
headers={'User-Agent':user_agent,}

request=urllib.request.Request(url,None,headers) #The assembled request
response = urllib.request.urlopen(request)

data = response.read()
soup = BeautifulSoup(data, features="html.parser")

# kill all script and style elements
for script in soup(["script", "style"]):
    script.extract()    # rip it out

# get text
text = soup.get_text()

# break into lines and remove leading and trailing space on each
lines = (line.strip() for line in text.splitlines())
# break multi-headlines into a line each
chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
# drop blank lines

translated_text = ""

for texty in chunks:
    if texty:
        print (texty)
        tranlation = translator.translate(texty)
        translated_text = translated_text + tranlation

print(translated_text)
#по сути, все что мне нужно для перевода -  НЛП для распознавания голоса
#Обучить машину переводить текст. В пизду. Половину апишек - платная. А половина с ограничениями.
#Либо пользоваться гугл переводчиком(только эта хуйня может к хуям тебя забанить. Ы-ы-ы
# Переводчик, что будет переводить нужную для меня шнягу
# Штука, что будет воспроизводить текст при помощи голоса. Шняги по голосу уже есть в большом
# количестве. Так что юзнуть какую-нибудь бесплатную библеотеку - будет весело.
# Ебануть подобие апишки, рофла ради \ А ведь по сути можно по просту сделать чат бота, что как раз будет спе
#циализироваться на предсказании того, какие слова на другом языке, похожие по смыслу пойдут
# дальше.
#Да сделать так, чтобы оно трогало только чужую речь, разделяла речи по их тембру, воспроизводила
# после на выбранном языке или том на котором сейчас говорили. После друг друга или до - хз

#Прочитать текст с экрана(Можно пиздить из html)
#Определить язык\перевести
#Попробовать вывести\заменить текст на сайте - файле, либо ебануть
#по кордам текста штуки, что нужно.
#
#


#Офлайн версия транслейта(Может она и быстрее и нормальнее будет работать.)


#import urllib.request
#urllib.request.urlretrieve('https://argosopentech.nyc3.digitaloceanspaces.com/argospm/translate-ru_en-1_0.argosmodel', 'translate-ru_en-1_0.argosmodel')

# Install it
#from argostranslate import package
#package.install_from_path('translate-ru_en-1_0.argosmodel')


#from argostranslate import translate

#def get_argos_model(source, target):
#lang = f'{source} -> {target}'
# source_lang = [model for model in translate.get_installed_languages() if lang in map(repr, model.translations_from)]
#  target_lang = [model for model in translate.get_installed_languages() if lang in map(repr, model.translations_to)]

#   return source_lang[0].get_translation(target_lang[0])

#argos_ru_en = get_argos_model('Russian', 'English')


#argos_ru_en.translate('что слишком сознавать — это болезнь, настоящая, полная болезнь.')
# "I think it's a disease, a real, complete disease."


#from transformers import MarianMTModel, MarianTokenizer
#from typing import Sequence

#class Translator:
# def __init__(self, source_lang: str, dest_lang: str) -> None:
#      self.model_name = f'Helsinki-NLP/opus-mt-{source_lang}-{dest_lang}'
#       self.model = MarianMTModel.from_pretrained(self.model_name)
#        self.tokenizer = MarianTokenizer.from_pretrained(self.model_name)

#def translate(self, texts: Sequence[str]) -> Sequence[str]:
#     tokens = self.tokenizer(list(texts), return_tensors="pt", padding=True)
#       translate_tokens = self.model.generate(**tokens)
#      return [self.tokenizer.decode(t, skip_special_tokens=True) for t in translate_tokens]


#marian_ru_en = Translator('ru', 'en')
#marian_ru_en.translate(['что слишком сознавать — это болезнь, настоящая, полная болезнь.'])
# Returns: ['That being too conscious is a disease, a real, complete disease.']


#import stanza

# First you will need to download the model
# stanza.download('ru')
#nlp = stanza.Pipeline('ru', processors='tokenize')

#for sentence in nlp.process('Сдается однокомнатная мебелированная квартира квартира. Ежемесячная плата 18 тыс.р. + свет.').sentences:
#   print(sentence.text)

# Сдается однокомнатная мебелированная квартира квартира.
# Ежемесячная плата 18 тыс.р. + свет.


#from dataclassess import dataclass

#@dataclass(frozen=True)
#class SentenceBoundary:
#text: str
# prefix: str

#  def __str__(self):
#       return self.prefix + self.text


#from __future__ import annotations # For Python 3.7
#from typing import List

#@dataclass(frozen=True)
#class SentenceBoundaries:
#sentence_boundaries: List[SentenceBoundary]

# @classmethod
#    def from_doc(cls, doc: stanza.Document) -> SentenceBoundaries:
#       sentence_boundaries = []
#      start_idx = 0
#for sent in doc.sentences:
#    sentence_boundaries.append(SentenceBoundary(text=sent.text, prefix=doc.text[start_idx:sent.tokens[0].start_char]))
#     start_idx = sent.tokens[-1].end_char
#  sentence_boundaries.append(SentenceBoundary(text='', prefix=doc.text[start_idx:]))
#   return cls(sentence_boundaries)

#@property
#def nonempty_sentences(self) -> List[str]:
#   return [item.text for item in self.sentence_boundaries if item.text]

#def map(self, d: Dict[str, str]) -> SentenceBoundaries:
#     return SentenceBoundaries([SentenceBoundary(text=d.get(sb.text, sb.text),
#  prefix=sb.prefix) for sb in self.sentence_boundaries])

#   def __str__(self) -> str:
#      return ''.join(map(str, self.sentence_boundaries))


#class Translator:
# def __init__(self, source_lang: str, dest_lang: str, use_gpu: bool=False) -> None:
#    self.use_gpu = use_gpu
# self.model_name = f'Helsinki-NLP/opus-mt-{source_lang}-{dest_lang}'
#  self.model = MarianMTModel.from_pretrained(self.model_name)
#   if use_gpu:
#        self.model = self.model.cuda()
#     self.tokenizer = MarianTokenizer.from_pretrained(self.model_name)
#      self.sentencizer = stanza.Pipeline(source_lang, processors='tokenize', verbose=False, use_gpu=use_gpu)

#   def sentencize(self, texts: Sequence[str]) -> List[SentenceBoundaries]:
#        return [SentenceBoundaries.from_doc(self.sentencizer.process(text)) for text in texts]

# def translate(self, texts: Sequence[str], batch_size:int=10, truncation=True) -> Sequence[str]:
#   if isinstance(texts, str):
#       raise ValueError('Expected a sequence of texts')
#   text_sentences = self.sentencize(texts)
# translations = {sent: None for text in text_sentences for sent in text.nonempty_sentences}

# for text_batch in minibatch(sorted(translations, key=len, reverse=True), batch_size):
#      tokens = self.tokenizer(text_batch, return_tensors="pt", padding=True, truncation=truncation)
#       if self.use_gpu:
#            tokens = {k:v.cuda() for k, v in tokens.items()}
#         translate_tokens = self.model.generate(**tokens)
#          translate_batch = [self.tokenizer.decode(t, skip_special_tokens=True) for t in translate_tokens]
#           for (text, translated) in zip(text_batch, translate_batch):
#                translations[text] = translated

#        return [str(text.map(translations)) for text in text_sentences]


#for translation in marian_ru_en.translate(['', '.', '!', '-', '&']):
#    print(translation)


#It's okay. It's okay, it's okay, it's okay.
#I don't know.
#Hey, hey, hey, hey, hey, hey, hey, hey, hey, hey, hey, hey, hey, hey, hey, hey, hey, hey, hey, hey, hey, hey, hey, hey, hey, hey, hey, hey, hey, hey, hey, hey, hey, hey, hey, hey, hey, hey, hey, hey, hey, hey, hey, hey, hey, hey, hey, hey, hey, hey, hey, hey, hey, hey, hey, hey, hey, hey, hey, hey.
#- Yeah, yeah, yeah, yeah, yeah, yeah, yeah, yeah, yeah, yeah, yeah, yeah, yeah, yeah, yeah, yeah, yeah, yeah, yeah, yeah, yeah, yeah, yeah, yeah, yeah, yeah, yeah, yeah, yeah, yeah, yeah, yeah, yeah, yeah, yeah, yeah, yeah, yeah, yeah, yeah, yeah, yeah, yeah, yeah.
#♪ I don't know ♪
