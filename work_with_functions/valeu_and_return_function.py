# 
# def toliq_ism_yasa(ism, familya):
#     """Toliq ism qaytaruvchi funksiya"""
#     toliq_ism= f"{ism} {familya}"
#     return toliq_ism
#     talaba = toliq_ism_yasa('olim', 'hakimov')

# def toliq_ism_yasa(ism, familya):
#     """Toliq ism qaytaruvchi funksiya"""
#     toliq_ism= f"{ism} {familya}"
#     return toliq_ism

# talaba1= toliq_ism_yasa('olim', 'hakimov')
# talaba2= toliq_ism_yasa('hakim', 'olimov')
# print(f"Darsga kelmagan talabalr royxati: {talaba1} va {talaba2}")
# print(f"{talaba1} darsga kechikib keldi")

# def toliq_ism_yasa(ism, familya, otasining_ismi=''):
#     """toliq ism qaytaruvchi funlsiya"""
#     if otasining_ismi:
#         toliq_ism= f"{ism} {otasining_ismi} {familya}"
#     else:
#         toliq_ism= f"{ism} {familya}"
#     return toliq_ism.title()

# talaba1 = toliq_ism_yasa('olim', 'hakimov')
# talaba2 = toliq_ism_yasa('hakim', 'abrorivich','olimov')
# print(f"Darsga kelmagan talabalr: {talaba1} va {talaba2}")  


# def avto_info(kompaniya, model, rangi, karobka, yili, narxi=None):
#     avto = {'kompaniya':kompaniya,
#             'model':model,
#             'rangi':rangi,
#             'karobka':karobka,
#             'yili':yili,
#             'narxi':narxi}
#     return avto
#     avto1 = avto_info('GM', 'malibu', 'qora', 'avtomat', 2018)
#     avto = avto_info('GM', 'gentera', 'oq', 'mexanika', 2016, 13000)
#     avtolar = [avto1, avto2]
#     print('onlayn bozordagi mavjud mashinalar:')
#     for avto in avtolar:
#         if avto ['narx']:
#             narx = avto['narx']
#         else:
#             narx = "Nomalum"
#             print(f"{avto['rang']} {avto['model']}. narxi: {narx}")

# # FUNKSIYADAN RO'YXAT QAYTARISH
# def oraliq(min, max):
#     sonalar = []
#     while min<max:
#         sonalar.append(min)
#         min += 1
#     return sonalar

# print(oraliq(0, 10))
# print(oraliq(10, 21))     

# def avto_info(kompaniya, model, rangi, karobka, yili, narxi=None):
#     avto = {'kompaniya':kompaniya,
#             'model':model,
#             'rangi':rangi,
#             'karobka':karobka,
#             'yili':yili,
#             'narxi':narxi}
#     return avto

# print("saytimizdagi avtolar royxatini shakllantiramiz.")
# avtolar = []
# while True:
#     print("\nQuyidagi malumotlarni kiriting",end='')
#     kompaniya=input("ishlab chiqaruvchi:")
#     model=input("modeli:")
#     rangi=input("rangi:")
#     karobka=input("karobka:")
#     yili=input("yili:")
#     narxi=input("narxi")

#     avtolar.append(avto_info(kompaniya, model, rangi, karobka, yili)) 

#     javob = input("yana avto qoshaszmi? (yes/no):")  
#     if javob =='no':
#         break

#     print("\nSalonimizdagi avtolar:")
#     for avto in avtolar:
#         if avto ['narx']:
#             narx = avto['narx']
#         else:
#             narx = "nomalum"
#         print(f"{avto['rang'].title()} {avto['model'].title()} {karobka} karobka. narxi: {narx}")    
