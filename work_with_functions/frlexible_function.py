# *args va **kwargs
# def summa(*sonlar):
#     """kiritilgan sonlarning yig'indisini hisoblaydigan funksiya"""
#     yigindi= 0
#     for son in sonlar:
#         yigindi+= son
#     return yigindi
# print(summa(1,2))
# print(summa(1,2,3,4,5))
# print(summa(4,5,6,7))    


# def avto_info(kompaniya, model, **malumotlar):
#     """Avto haqidagi ma'lumotlarni lug'at ko'rinishida qaytaruvchi funksiya"""
#     malumotlar['kompaniya']=kompaniya
#     malumotlar['model']=model
#     return malumotlar

# avto1 = avto_info("GM", "malibu", rang= 'qora', yil=2018)
# avto2 = avto_info("Kia", "K5", rang='qizil', narx=35000, yil=2020, karobka='avtomat')

