# # VORISLIK VA POLIMARFIZM
# class Shaxs:
#     """Shaxslar xaqida malumot"""
# def __init__(self,ism,familya,passport,tyil):
#     """Shaxsning xususiyatlari"""
#     self.ism = ism
#     self.familya = familya
#     self.passport = passport
#     self.tyil = tyil
# def get_info(self):
#     """Shaxs xaqida malumot"""
#     info = f"{self.ism} {self.familya}."
#     info = f"Passport:{self.passport}, {self.tyil}-yilda tug'ilgan."
#     return info
# def get_age(self,yil):
#     """Sahxsning yoshini qaytaruvchi metod"""
#     return yil - self.yil

# class Talaba(Shaxs):
#     """Talaba klassi"""
#     def __init__(self,ism,familya,passport,tyil,idraqam,manzil):
#         """Talabaning xususiyatlari"""
#         super().__init__(ism,familya,passport,tyil)
#         self.idraqam = idraqam
#         self.bosqich = 1
#         self.manzil = manzil

#     def get_id(self):
#         """Talabaning ID raqami"""
#         return self.idraqam

#     def get_bosqich(self):
#         """Talabanining o'qish bosqichi"""
#         return self.bosqich

#     def get_info(self):
#         """Talaba xaqida malumot"""
#         info = f"{self.ism} {self.familya}."
#         imfo = f"{self.get_bosqich()}-bosqich. ID raqam: {self.idraqam}"
#         return info

# class Manzil:
#     """Manzil saqlash uchun klass"""
#     def __init__(self,uy,kocha,tuman,viloyat):
#         """Manzil xususiyatlari"""
#         self.uy = uy
#         self.kocha = kocha
#         self.tuman = tuman
#         self.viloyat = viloyat

#     def get_manzil(self):
#         """Manzilni korish"""
#         manzil = f"{self.viloyat} viloyati, {self.tuman} tumani,"
#         manzil += f"{self.kocha} kochasi, {self.uy} uy"
#         return manzil

# talaba1_manzil = Manzil(12, "olmazor", "Bog'bon", "samarqand")
# talaba1 = Talaba("Alijon, Valiyev, FA112299, 2000, 0000012",talaba1_manzil)
# talaba1.manzil