# -*- coding: utf-8 -*-

#Tuple = Demet
#
#- Kapsayıcıdır.
#- Sıralıdır.
#- DEĞİŞTİRİLEMEZLER.

#- () ve tuple() İçerisine yazılır tuple - demet

#Erişim işlemleri Listelerle aynıdır.
#Ama sadece içerisindeki veriler DEĞİŞTİRLEMEZ

#tuple oluşturme
tupleListe = (2,4,6,"Osmaniye",(1,2,3),[])
liste = [2,4,6,"Osmaniye",[5,8,9],()]

# Tuple da listede bir değişiklik yapılmaz...
#tupleListe[0]=8

liste[0]= 9

##  -2 ile Tuple ve listenin içindeki en sağdan 2 ikinciyi listeleri gösteriyor
print(tupleListe[-2])
print(liste[-2])


print(type(tupleListe))
print(type(liste))
print(tupleListe)
print(liste)
print(len(tupleListe))
print(len(liste))
 
