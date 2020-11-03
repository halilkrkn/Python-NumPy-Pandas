

#NESNE YONELIMLI PROGRAMLAMA

#Sinif Nedir?
    

    

#Sinif Ozellikleri (Class attributes)

class VeriBilimci():
    bolum = ''
    sql = 'Evet'
    deneyim_yili = 0
    bildigi_diller = []
    
#Siniflarin ozelliklerine erismek
VeriBilimci.bolum
VeriBilimci.sql

#siniflarin ozelliklerini degistirmek
VeriBilimci.sql = "Hayir"
VeriBilimci.sql

#Sinif Orneklendirmesi (instantiation)

ali = VeriBilimci()

ali.sql
ali.deneyim_yili
ali.bolum
ali.bildigi_diller.append("Python")
ali.bildigi_diller

veli = VeriBilimci()
veli.sql

veli.bildigi_diller

#Ornek ozellikleri

class VeriBilimci():
    bildigi_diller = ["R","PYTHON"]
    bolum = ''
    sql = ''
    deneyim_yili = 0
    def __init__(self):
        self.bildigi_diller = []
        self.bolum = ''

ali = VeriBilimci()
ali.bildigi_diller

veli = VeriBilimci()
veli.bildigi_diller

ali.bildigi_diller.append("Python")
ali.bildigi_diller

veli.bildigi_diller
veli.bildigi_diller.append("R")
veli.bildigi_diller

VeriBilimci.bildigi_diller
ali.bolum

VeriBilimci.bolum
ali.bolum = "istatistik"
VeriBilimci.bolum
veli.bolum
veli.bolum = "end_muh"
veli.bolum
ali.bolum
VeriBilimci.bolum

#Ornek Metodlari

class VeriBilimci():
    calisanlar = []
    def __init__(self):
        self.bildigi_diller = []
        self.bolum = ''
    def dil_ekle(self, yeni_dil) :
        self.bildigi_diller.append(yeni_dil)


ali = VeriBilimci()
ali.bildigi_diller
ali.bolum

veli = VeriBilimci()
veli.bildigi_diller
veli.bolum

dir(VeriBilimci)

VeriBilimci.dil_ekle
VeriBilimci.dil_ekle("R")

ali.dil_ekle("R")
ali.bildigi_diller

veli.dil_ekle("Python")
veli.bildigi_diller

#Miras Yapilari (inheritance)

class Employees():
    def __init__(self):
        self.FirstName = ""
        self.LastName = ""
        self.Address = ""

class DataScience(Employees):
    def __init__(self):
        self.Programming = ""

veribilimci1 = DataScience()
#veribilimci1.

class Marketing(Employees):
    def __init__(self):
        self.StoryTelling = ""

mar1 = Marketing()
#mar1.


class Employee_yeni():
    def __init__(self, FirstName,LastName,Address):
        self.FirstName = FirstName
        self.LastName = LastName
        self.Address = Address


ali = Employee_yeni("a","b","c")
ali.FirstName
