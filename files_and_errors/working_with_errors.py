# XATOLAR BILAN ISHLASH
# import json
# files = ['talaba1.json','talaba2.json','talaba3.json','talaba2.json']
# for filename in files:
#     try:
#         with open(filename) as f:
#             talaba = json.load(f)
#     except FileNotFoundNameError:
#         pass
#     else:
#         print(talaba['ism'])
        
# n = input("Butun son kiriting")
# try:
#     n = int(n)
#     x = 20/n

# except ValueError:
#     print("Butun son kiritmadingiz")
# except ZeroDivisionError:
#     print("0 ga bo'lish mumkin emas")
# else:
#     print(f"x={x}")

# while True:
#     yosh = input("Yoshingizni kiriting")
#     if yosh.isdigit():
#         yosh = int(yosh)
#         break

# print(f"Siz {2021-yosh} yilda tug'ilgansiz")


# yosh = input("Yoshingizni kiriting:")

# try :
#     yosh = int(yosh)
# except:
#     print("Siz butun son kiritmadingiz")
# else:
#     print(f"Siz {2021-yosh} yilda tug'ilgansz")

# print("Dastur davom etyapti")
# print("Dastur tugadi")


# # ZeroDevisionError
# x,y = 5,10
# try:
#     y/(x-5)
#     except ZeroDevisionError:
#         print("0 ga bo'lish mumkin emas")


# # IndexError
# mevalar = ['olma','anor','anjir','uzum']
# try:
#     print(mevalar[2])
# except IndexError:
#     print(f"Ro'yxatda {len(mevalar)} ta meva bor xolos")


# KeyError
# user = {"username":"sariqdev",
#         "status":"admin",
#         "email":"admin@sariq.dev",
#         "phone":"998931234567"}

# key = 'tel'
# try:
#     print(f'Foydalanuvchi: {user[key]}')
# except KeyError:
#     print("Bunday kalit mavjud emas")

# print(user['username'])


# import pickle

# with open('info','rb') as file:
#     talaba1 = pickle.load(file)
#     talaba2 = pickle.load(file)

# print(talaba1)
# print(talaba2)
# filename = "data.txt"
# try:
#     with open(filename) as f:
#         text = f.read()
# except FileNotFoundError:
#     print(f"{filename} mavjud emas")






