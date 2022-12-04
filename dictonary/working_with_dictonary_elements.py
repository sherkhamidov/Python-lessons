# ITEMS
# talaba_0 = {
#     'ism':'alijon',
#     'familya':'shamsiyev',
#     'yosh':'22',
#     'kurs':'4',
#     'fakultet':'tarjimonlik'
#     }
# print(talaba_0.items())    
# for kalit, qiymat in talaba_0.items():
#     print(f"Kalit: {kalit}")
#     print(f"qiymat: {qiymat}")


# telefonlar = {
#         'ali':'ipone x',
#         'vali':'samsung s9',
#         'husan':'redmi 10',
#         'akmal':'nokia 3310'
#         }
# for k, q in telefonlar.items():
#     print(f"{k.title() }ning telefoni{q}")       


# KEYS
# mahsulotlar = {
#     'olma':10000,
#     'orik':5000,
#     'uzum':20000,
#     'anor':15000,
#     'shaftoli':20000,
#     }
# print(mahsulotlar.keys())
# print('Do\'kondagi mahsulotlar:')
# for mahsulotlar in mahsulotlar.keys():
#     print(mahsulotlar.title())


# print('Do\'kondagi mahsulotlar:')
# for mahsulotlar in mahsulotlar:
#     print(mahsulotlar.title())



# bzorlik = ['anor', 'uzum', 'non', 'baliq']
# for mahsulot in mahsulotlar:
#     if buyum not in mahsulotlar:
#         print(f"{mahsulot.title()} {mahsulotlar [mahsulot]} som")

# for buyum in bozorlik:
#     if buyum not in mahsulotlar:
#         print(f"Do\'koningizga {buyum} ham olib keling")


# LUGAT ELEMENTLARINI TARTIB BN CHIQARISH
# print("Do\'konimizdagi mahsulotlar:")
# for mahsulot in sorted(mahsulotlar):
#     print(mahsulot.title())


# values
# print(telefonlar.values())

# print('foydalanuvchilar quydagi telefonlarni ishlatadi:')
# for tel in telefonlar.values():
#     print(tel)

#     telefonlar = {
#         'jamshid','iphone x',
#         'ali','redmi',
#         'vali','nokia',
#         'hasan','pocco',
#         'mar','iphone 12',
#         'johon','galaxy 21',
#         'shodiyor','redmi 9'
#         }
# print("Foydalanuvchilar quydagi telefonlarni ishlatadi:")
# for tel in set(telefonlar.values()):
#     print(tel)


# toys = {"ball", "car" "bear", "ball", "lamp"}



# NESTING'model':'lacetti',
#     'rang':'oq',
#     'narx':13000,
#     'yil':2016,
#     'km':50000,
#     'karobka':'avtomat'
#         }

# car1 = {
# car0 = {
#     
#     'model':'gentera',
#     'rang':'oq',
#     'narx':15000,
#     'yil':2018,
#     'km':20000,
#     'karobka':'avtomat'
#     }

# car2 = {
#     'model':'malibu',
#     'rang':'qora',
#     'narx':23000,
#     'yil':2022,
#     'km':10000,
#     'karobka':'avtomat'
#     }

# car= car0
# print(f"{car['model'].title()},"
#     f"{car['rang']} rang, "
#     f"{car['yil']}-yil, {car['narx']}$")


# cars = [car0, car1, car2]
# for car in cars:
#     print(f"{car['model'].title()}, "
#     f"{car['rang']} rang, "
#     f"{car['yil']} -yil  {car['narx']}$")



# print(f"{cars[2]['rang'].title()}"
#     f"{cars[2]['model']}")


# malibus = []
# for n in range(10):
#     new_car = {
#         'model':'malibu',
#         'rang':'none',
#         'yil':2020,
#         'narx':'none',
#         'km':0,
#         'karobka':'avto'
#          }
        
#     malibus.append(new_car)
     
# for malibu in malibus:
#     print(malibu)

#     for malibu in malibus[:3]:
#         malibu['rang']='qizil'

#     for malibu in malibus:
#         print(malibu)

# for malibu in malibus:
#     malibu['rang']='qora'

#     for malibu in malibus:
#         print(malibu)

#     for malibu in malibus:
#         malibu['rang']='oq'
#         malibu['karobka']='mexanika'


#         for malibu in malibus:
#             if malibu['karobka']== 'avto':
#                 malibu['narx']=40000
#             else:
#                 malibu['narx']=35000

#             for malibu in malibus:
#                 print(malibu)


# LUG'AT ICHIDA RO'YXAT
# dasturchilar = {
#     'ali':['pyton','c++'],
#     'vali':['html','css','js'],
#     'hasan':['php','sql'],
#     'husan':['python','php'],
#     'maryam':['c++','c#']
#     }

# for ism,tillar in dasturchilar.items():
#     print(f"\n{ism.title()} quyidagi dasturlash tillarini biladi")
#     for til in tillar:
#         print(til.upper())

# for ism, tillar in dasturchilar.items():
#     print(f"\n{ism.title()} quydagi dasturlash tillarini biladi")
#     for til in tillar:
#         print(f'{til.upper()} ', end='')

# hamkasblar= {
# 'ali':{'familya':'valiyev',
#     'tyil':1995,
#     'malumot':'oliy',
#     'tillar':['python', 'c++']
# },
# 'vali':{'familya':'aliyev',
#     'tyil':2001,
#     'malumot':'o\'rta-maxsus',
#     'tillar':['html', 'css','js']},
# 'hasan':{'familya':'husanov',
#     'tyil':2002,
#     'malumot':'maxsus',
#     'tillar':['python', 'php']}
#     }


# for ism, info in hamkasblar.items():
#     print(f"\n{ism.title()} {info['familya'].title()}, "
#         f"{info['tyil']}-yilda tug'ilgan. "
#         f"Malumoti:{info['malumot']}. \n"
#         "Quyidagi dasturlash tillarini biladi:")
#     for til in info['tillar']:
#         print(til.upper())       





