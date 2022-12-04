# # 
import datetime as dt

# hozir = dt.datetime.now()
# print(hozir)

# # date
# bugun = dt.date.today()
# print(f"Bugungi sana: {bugun}")
# ertaga = dt.date(2021,3,10)
# print(f"Ertangi sana {ertaga}")

# # time
# hozir = dt.datetime.now()
# vaqtHozir = hozir.time()
# print(f"Hozir soat: {vaqtHozir}")
# vaqtKeyin = dt.time(23.45,30)
# print(vaqtKeyin)

# # Sanalar orasidagi farq
# bugun = dt.date.today()
# ramazon = dt.date(2021,4,13)
# farq = ramazon - bugun

# print(f"Ramazonga {farq.days} kun qoldi")


# # Soatlar orasidagi farq
# hozir = dt.datetime.now()
# futbol = dt.datetime(2021, 3, 10, 23, 45, 00)
# farq = futbol-hozir
# sekundlar = farq.seconds
# minutlar = int(sekundlar/60)
# soatlar = int(minutlar/60)
# print(f"Futbol boshlanishiga {farq.days} kunu {soatlar} soat qoldi")

# math
# import math
# PI = math.pi
# print(f"Pi ning qiymati: {PI}")
# E = math.e
# print(f"E ning qiymati: {E}")

# # trigonometrya
# math.sin(math.pi/2)
# math.cos(0)
# math.tan(PI)

# # radianlar va burchaklar ortasidagi konvertasiya
# print(math.degrees(math.pi/2))
# print(math.radians(90))

# # sonlarni yaxlitlash
# x = 4.6
# print(math.ceil(x))
# print(math.floor(x))

# # kvadrat ildiz
# x = 81
# math.sqrt(x)

# # Darajaga oshirish
# math.pow(x, 3)
# math.pow(x, 5)
# math.pow(x, 1/3)

# from pprint import pprint
# import json

# filename = 'bemor.json'
# with open(filename) as f:
#     bemor = json.load(f)

# pprint(bemor)

# RegEx
import re
from words_list import words

# word1 = "темир"
# word2 = "томир"
# word3 = "тулпор"

# andoza = "^т...р"

# print(re.match(andoza, word1))
# print(re.match(andoza, word2))
# print(re.match(andoza, word3))

# matches = []
# for word in words:
#     if re.match(andoza, word):
#         matches.append(word)

# print(matches)


# matches = []
# for word in words:
#     if re.match(abdoza,word):
#         matches.append(word)

# print(matches)
# # kuchli parolni tekshirish
# andoza = '^([a-z0-9][-a-z0-9_\+\.]*[a-z0-9])@([a-z0-9][-a-z0-9\.]*[a-z0-9]'
# msg = "yangi parol kiriting"
# msg += '(kamida 8 bejgidan iborat, kamida bitta lotin bosh harf, 1 ta kichik harf,'
# msg += '1 ta son va 1 ta maxsus belgi bolid=shi kerak): '
# while True:
#     password = input(msg)
#     if re.match(andoza, password):
#         print("Maxfiy so'z qabul qilindi")
#         break
#     else:
#         print("Maxfiy so'z talabga javob bermadi")
