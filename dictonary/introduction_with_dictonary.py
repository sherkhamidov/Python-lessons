# DICTONARY
# car_0 = {'model':'ferrari','rang':'qizil'}
# print(car_0['model'])
# print(car_0['rang'])


# en_uz = {'apple':"olma", 'apricot':"shaftoli", 'plane':"samalyot"}
# print(en_uz)


# mevalar= {'olma':10000,'tarvuz':8000,'qovun':10000}
# print(f"Olmanarxi {mevalar['olma']} so'm")
# print(mevalar['tarvuz'])


# talaba_0= {'ism':'murod olimov','yosh':20,'t_yil':2000}
# print(f"{talaba_0['ism'].title()},\
#     {talaba_0['t_yil']}-yilda tug'ilgan,\
#     {talaba_0['yosh']} yoshda")    


# # YANGI KALIT SO'Z VA QIYMAT QO'SHISH
# talaba_0['kurs'] = 4
# talaba_0['fakultet'] = 'informatika'
# print(talaba_0)


# BO'SH LUG'AT
# talaba_1 = {}
# talaba_1['ism'] = 'qobil rasulov'
# talaba_1['kurs'] = 3
# talaba_1['yosh'] = 20
# print(talaba_1)
# print(f"Talaba{talaba_1[ism].title()} {talaba_1['kurs']}-kurs")


# # QIYMATNI YANGILASH
# talaba_1['kurs'] = 4
# print(f"Talaba{talaba_1['ism'].title()} {talaba_1['kurs']}-kurs")


# KALIT SOZ-QIYMATNI O'CHIRIB TASHLASH
# talaba_0 = {'ism':'murod olimov','yosh':20,'t_yil':2000}
# print(talaba_0)
# del talaba_0['yosh']
# print(talaba_0)


# LUG'ATLARDA BIR NECHTA QATORDA YOZISH
# telefonlar = {
#     'ali':'ipone x',
#     'vali':'glaxy s9',
#     'olim':'mi 10pro',
#     'orif':'nokia 3310',
#     'anvar':'pocco 3x'
#      }


# GET METODI
# phone = telefonlar['ali']
# print(f"alining telfoni{phone}")


# phone = telefonlar['hasan']
# print(f"hasanning telefoni{phone}")

# meva = en_uz.get('apple','Bunday ism mavjud emas')
# # print(meva)

# phone = telefonlar.get('hasan')
# print(phone)