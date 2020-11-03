#%% Basics
class Matematik:
    def __init__(self,sayi1,sayi2): # Constructer Bloğu
        print("çalıştı")
        self.sayi1 = sayi1
        self.sayi2 = sayi2
    def topla(self):
        return self.sayi1 + self.sayi2

    def cıkar(self):
        return self.sayi1 + self.sayi2

    def carp(self):
        return self.sayi1 + self.sayi2

    def bol(self):
        return self.sayi1 + self.sayi2

matematik = Matematik(2,78)   
matematik2 = Matematik(2,76)
ToplaSonuc = matematik.topla()
print(ToplaSonuc)
#%% Property = Özellik
class Person:
    def __init__(self,firstName,LastName,age):
        self.firstName = firstName
        self.LastName = LastName
        self.Age = age

person1 = Person("halil","karkın",24)  
print(person1.firstName)   
#%% Inheritance = Miras Yapısı

class Worker(Person):
    def __init__(self,salary):
        self.salary = salary

class Customer(Person):
    def __init__(self,creditCardNumber):
        self.creditCardNumber = creditCardNumber

ahmet = Worker()
mehmet = Customer()
mehmet.