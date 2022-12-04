# #INKAPSULATSIYA VA KLASSGA OID XUSUSIYAT VA METODLAR
# from uuid import uuid4
# class Avto:
#     """Avtomabil klassi"""
#     def __init__(self,make,model,rang,narx,km=0):
#         self.make = make
#         self.model = model
#         self.rang = rang
#         self.narx = narx
#         self.__km = km
#         self.__id = uuid4()

        
#     def get_km(self):
#         return self.__km

#     def get_id(self):
#         return self.__id

#     def add_km(self,km):
#         """Mashinaning km ga yna km qo'shish"""
#         if km>=0:
#             self.__km += km
#         else:
#             print("Moshinaning km ni kamaytirib bo'lmaydi")
            

# from uuid import uuid4
# class Avto:
#     """Avtomabil klassi"""
#     __num_avto = 0
#     def __init__(self,make,model,rang,yil,narx,km=0):
#         """Avtomobilning xususiyatlari"""
#         self.make = make
#         self.model = model
#         self.rang = rang
#         self.yil = yil
#         self.narx = narx
#         self.__km =km
#         self.__id = uuid4()
#         Avto.__num_avto += 1

#     @classmethod
#     def get_num_avto(cls):
#         return cls.__num_avto
    
#     def get_km(self):
#         return self.__km

#     def get_id(self):
#         return self.__id

#     def add_km(self,km):
#         """Mashinaning km ga yana km qoshish"""
#         if km>=0:
#             self.__km += km
#         else:
#             print("Mashina km kamaytirib bo'lmaydi")
# avto1 = Avto("GM", "Malibu","qora",2020,40000) 
# avto2 = Avto("GM", "Lacetti","oq",2020,20000)
# avto3 = Avto("Tayota", "Carolla","silver",2020,50000)
# print(Avto.get_num_avto())


# import avto

# avto1 = avto.Avto("GM", "Malibu","qora",2020,40000) 
# avto2 = Avto("GM", "Lacetti","oq",2020,20000)
# avto3 = Avto("Tayota", "Carolla","silver",2020,50000)
# print(Avto.get_num_avto())
