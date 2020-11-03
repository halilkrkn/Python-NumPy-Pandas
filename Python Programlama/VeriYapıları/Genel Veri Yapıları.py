#VERI YAPILARI

#Listeler 

#[]
#list()

notlar = [90,80,70,50]
type(notlar)

liste = ["a",19.3,90]
list_genis = ["a",19.3,90, notlar]

len(list_genis)

list_genis[0]
list_genis[1]
list_genis[3]

type(list_genis[3])

tum_liste = [liste, list_genis]

#del tum_liste

#Listeler - Eleman Islemleri


liste = [10,20,30,40,50]

liste[0]
liste[1]

liste[6]

liste[0:2]

liste[:2]

liste[2:]

yeni_liste = ["a",10,[20,30,40,50]]
yeni_liste

yeni_liste[2]

yeni_liste[0:2]

yeni_liste[2][1]

#Listeler - Eleman Degistirme

liste = ["ali","veli","berkcan","ayse"]
liste

liste[1] = "velinin_babasi"

liste

liste[1] = "veli"

liste[0:3] = "alinin_babasi","velinin_babasi","berkcanin_babasi"  

liste

liste = ["ali","veli","berkcan","ayse"]
liste

liste = liste + ["kemal"]
liste

#del liste[2]
liste

#Listeler - Liste Metodları

liste = ["ali","veli","isik"]

dir(liste)

liste

#append & remove

liste.append("berkcan")

liste

liste.remove("berkcan")
liste

# insert 

liste = ["ali","veli","isik"]

liste

liste.insert(0,"ayse")

liste

liste = ["ali","veli","isik"]

liste[0] = "ayse"

liste

liste.insert(0,"ayse")
liste

liste[1] = "ali"

liste

liste.insert(2,"mehmet")
liste

liste.insert(5,"berk")
liste

len(liste)


liste.insert(len(liste),"beren")
liste

#pop 


liste.pop(0)
liste

liste.pop(4)
liste

#count

liste = ["ali","veli","isik","ali","veli"]

liste.count("ali")
liste.count("veli")
liste.count("isik")

#copy

liste_yedek = liste.copy()

#extend

liste.extend(["a","b",10])
liste

#index()

liste.index("ali")

#reverse()

liste.reverse()
liste

#sort()

liste = [10,40,5,90]
liste.sort()
liste

#clear

liste.clear()
liste


#Veri Yapıları - Tuple

#Tuple Olusturma

t = ("ali","veli",1,2,3.2,[1,2,3,4])

t = "ali","veli",1,2,3.2, [1,2,3,4]

#tuple()

t = ("eleman",)
type(t)

#Tuple Eleman Islemleri

t = ("ali","veli",1,2,3, [1,2,3,4])
t

t[1]
t[0:3]

t[2] = 99

# Veri Yapıları - Dictionary (Sözlük)


#Sozluk Olusturma
sozluk = {"REG" : "Regresyon Modeli",
          "LOJ" : "Lojistik Regresyon",
          "CART" : "Classification and Reg"}

sozluk

len(sozluk)


sozluk = {"REG" : 10,
          "LOJ" : 20,
          "CART" : 30}

sozluk


sozluk = {"REG" : ["RMSE",10],
          "LOJ" : ["MSE", 20],
          "CART" : ["SSE",30]}

sozluk

#Sozluk Eleman Islemleri

sozluk = {"REG" : "Regresyon Modeli",
          "LOJ" : "Lojistik Regresyon",
          "CART" : "Classification and Reg"}


sozluk[0]

sozluk["REG"]
sozluk["LOJ"]

sozluk = {"REG" : ["RMSE",10],
          "LOJ" : ["MSE", 20],
          "CART" : ["SSE",30]}


sozluk["REG"]

sozluk = {"REG" : {"RMSE": 10,
                   "MSE" : 20,
                   "SSE" : 30},

          "LOJ" : {"RMSE": 10,
                   "MSE" : 20,
                   "SSE" : 30},
                   
          "CART" : {"RMSE": 10,
                   "MSE" : 20,
                   "SSE" : 30}}

sozluk
sozluk["REG"]["SSE"]

#Sozluk - Eleman Eklemek & Degistirmek

sozluk = {"REG" : "Regresyon Modeli",
          "LOJ" : "Lojistik Regresyon",
          "CART" : "Classification and Reg"}

sozluk["GBM"] = "Gradient Boosting Mac"
sozluk

sozluk["REG"] = "Coklu Dogrusal Regresyon"
sozluk

sozluk[1] = "Yapay Sinir Aglari"

sozluk

l = [1]
l

sozluk[l] = "yeni bir sey"

t = ("tuple",)

sozluk[t] = "yeni bir sey"
sozluk

#Veri Yapilari - Setler

#Set olusturmak

s = set()
s

l = [1,"a","ali", 123]
s = set(l)
s


t = ("a","ali")

s = set(t)
s

ali = "lutfen_ata_bak ma_uza ya_git"
type(ali)

s = set(ali)
s

l = ["ali", "lutfen", "ata", "bakma", "uzaya",
     "git", "git", "ali","git"]

l

s = set(l)
s

len(s)

l[0]

s[0]



# Eleman ekleme & cikarma

l = ["gelecegi","yazanlar"]

s = set(l)

s

dir(s)

s.add("ile")
s

s.add("gelecege_git")
s

s.add("ile")
s

s.remove("ali")
s

s.discard("ali")

#Setler - Klasik Kume Islemleri

# =============================================================================
# difference() ile iki kumenin farkini ya da "-" ifadesi
# intersection() iki kume kesisimi ya da "&" ifadesi
# union() iki kumenin birlesimi
# symmetric_difference() ikisinde de olmayanlari.
# =============================================================================


#difference

set1 = set([1,3,5])
set2 = set([1,2,3])

set1.difference(set2)

set2.difference(set1)

set1.symmetric_difference(set2)

set1 - set2
set2 - set1

#intersection & union

set1 = set([1,3,5])
set2 = set([1,2,3])

set1.intersection(set2)
set2.intersection(set1)


kesisim = set1 & set2
kesisim

birlesim = set1.union(set2)
birlesim

set1.intersection_update(set2)
set1


#Set Sorgu Islemleri

set1 = set([7,8,9])
set2 = set([5,6,7,8,9,10])

#iki kumenin kesisiminin bos olup 
#olmadiginin sorgulanması

set1.isdisjoint(set2)


#bir kumenin butun elemanlarinin baska bir kume
#icerisinde yer alip almadigi

set1.issubset(set2)

#bir kumenin bir diger kumeyi kapsayip kapsamadigi

set2.issuperset(set1)




dir(str)