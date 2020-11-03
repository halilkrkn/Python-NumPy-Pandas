# -*- coding: utf-8 -*-

#substring
mesaj = "Merhaba Dünya"

print(mesaj[2:5])

yenimesaj = mesaj[2:]
print(yenimesaj)

yenimesaj2 = mesaj[12:13]
print(yenimesaj2)

##length

print(len(mesaj))
yenimesaj3 = mesaj[len(mesaj)-1:len(mesaj)]
print(yenimesaj3)

##lower upper

print(mesaj.upper())
print(mesaj.lower())


## Replace
print(mesaj.replace("ü","u"))
print(mesaj.replace("a","e"))

## Split = boşluğa göre ayırma
bilgi = " halil karkin 80 Düziçi "
print(bilgi.split())
print(bilgi.split(" "))

bilgi2 = "  Engin;Demiroğ;33;Ankara".strip()
print(bilgi2.split())
print("adi = "+ bilgi2.split(";")[0])

# Input 

ad= input("adiniz=")
sayi1 = input("sayi1 = ")
sayi2 = input("sayi2= ")

print (int(sayi1) + int(sayi2))