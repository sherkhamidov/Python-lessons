# pip install googletrans==3.1.0a0
# from googletrans import Translator
# tarjimon = Translator()

# matn_uz = "Python dunyodagi eng mashxur dasturlash tili"

# tarjima = tarjimon.translate(matn_uz)

# print(tarjima.origin)

# print(tarjima.text)

# print(tarjima.src)

# tarjima_ru = tarjimon.translate(matn_uz, dest='ru')
# print(tarjima_ru.text)

# matn_en = "Tashkent is the capital of Uzbekisatan"
# tarjima_uz = tarjimon.translate(matn_en, dest='uz')
# print(tarjima_uz.text)

# from googletrans import Translator
# tarjimon = Translator()

# msg = "Tarjima uchun so'z kiriting(chiqib ketish uchun \"q\" deb yozing):"
# while True:
#     text = input(msg)
#     if text == "q":
#         break
#     else:
#         tarjima = tarjimon.translate(text, src='uz', dest='en')
#         print(tarjima.text)


# # requests
import requests



# sahifa = "https://kun.uz/news/main"
# r = requests.get(sahifa)
# pprint(r.text)


# # restcountries API
# country = "Uzbekistan"
# url = f"https://restcountries.eu/rest/v2/name/{country}"
# r = requests.get(url)
# r_json = r_json()[0]
# print(r_json.keys())
# print(r_json['capital'])

import requests
# import googletrans

# url = "https://api.adviceslip.com/advice"
# r = requests.get(url)
# advice = r.json()['slip']['advice']
# print(advice)

# translator = googletrans.Translator()
# tarjima = translator.translate(advice, dest='uz')
# print(tarjima.text)

# import requests
# from bs4 import BeautifulSoup

# sahifa = "https://kun.uz/news/main"
# r = requests.get(sahifa)

# soup = BeautifulSoup(r.text, 'html.parser')

# news = soup.find_all(class_="new-title")
# print(news[0].text)


# import requests
# from bs4 import BeautifulSoup
# from wordcloud import WordCloud
# import matplotlip.pyplot as plt


# sahifa = "https://kun.uz/news/main"
# r = requests.get(sahifa)

# soup = BeautifulSoup(r.text,'html.parser')

# news = soup.find_all(class_="news-title")
# matn =""
# for n in news:
#     matn+=n.text

# stopwords = ["учун","буйича","лекин"]
# wordcloud = WordCloud(width=1000, height = 1000,)


# from fuzzywuzzy import fuzz
# from fuzzywuzzy import process
# from uzwords import words

# print(fuzz.ratio("salom","assalom"))
# print(fuzz.ratio("salom","salim"))


# Matnlar orasidan eng o'xshashini toping
# text = "талба"
# match = process.extractOne(text,words)
# print(match)


#
