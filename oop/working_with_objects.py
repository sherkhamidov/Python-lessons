# # # WORKING WITH OBJECTS
# def set_bosqich(self,yangi_bosqich):
#     """Yalabaning kursini yangilovchi metod"""
#     self.bosqich = yangi_bosqich

# def update_bosqic(self):
#     """Talabaning bosqichini bittaga ko'paytirish"""
#     self.bosqich += 1

# def get_info(self):
#     """Talaba haqida ma'lumot"""
#     return f"{self,ism} {self,familya}. {self,bosqich}-bosqich talabasi"
    
# def get_name(self):
#     """Talabaning ismini qaytaradi"""
#     return self.ism

# def get_lastname(self):
#     """Talabaning familyasini qaytaradi"""
#     return self,familya

# def get_age(self):
#     """Talabaning yoshini qaytarad"""
#     return yil-self.tyil

# class Fan():
#     """Fan nomli klass"""
#     def__init__(self,nomi)
#     self.nomi = nomi
#     self.talabalar_soni = 0
#     self.talabalar = []

# def add_student(self,talaba):
#     """Fanga talabalar qo'shish"""
#     self.talabalar.append(talaba)
#     self.talabalar_soni += 1

# def get_name(self):
#     """Fan nomi"""
#     return self,nomi

# def get_students(self):
#     """Fanga yozilgan talabalar haqida malumot"""
#     return [talaba.get_fullname() for x in self.talabalar]

# def get_students_num(self):
#     """Fanga yozilgan talabalar soni"""
#     return self.talabalar_soni

# def see_methods(klass):
#     return [method for methodin dir(klass)] if method.startswith('__') 


# Matematika = Fan("Oliy matematika")
# talaba1 = Talaba("alijon","valiyev",2000)
# talaba2 = Talaba("hasan","alimov",2001)
# talaba3 = Talaba("akrom","boriyev",2001)
# matematika.add_student(talaba1)
# matematika.add_student(talaba2)
# matematika.add_student(talaba3)
# print(matematika.talabalar_soni)