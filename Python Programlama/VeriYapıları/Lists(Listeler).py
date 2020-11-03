
#Listeler = Lists
# - Değiştirilebilirdir
# - Kapsayıcıdır(farklı tipte verileri tutabilir)
# - Sıralıdır

#******LİSTE OLUŞTURMA*****
# *[] ve list() formatında liste oluşturulur



ogrenciler = ["halil","KArkin",24]
print(ogrenciler[2])
ogrenciler.append("Musa")
ogrenciler.append(35)
ogrenciler.remove(35)
ogrenciler[0] = "göktuğ"
print(ogrenciler)
print(len(ogrenciler))

# List Constructer = liste oluşturucu
sehirler = list(("Ankara", "İstanbul","Adana"))
print(sehirler)
print(len(sehirler))


##Diğerr Fonksiyonlar

#Clear FONK.
#print(sehirler.clear()) # liste temizlendi clear fonk. ile
#print(sehirler)

#%%Count
print("Ankara Sayisi = " + str(sehirler.count("Ankara")))
print("Ankara indexi = " + str(sehirler.index("Ankara")))
#%%pop
sehirler.pop(1)
#%%insert
sehirler.insert(2,"İstanbul")
print(sehirler)
#%%reverse
sehirler.reverse()
print(sehirler)

#%%copy
sehirler3 = sehirler.copy()
sehirler2 = sehirler
#
sehirler2[0] = "izmir"
print(sehirler2)
print(sehirler)
print(sehirler3)

##%% extend
sehirler.extend(sehirler3)
print(sehirler)

#%% Sort = normal sıralmaa
#
sehirler.sort()
print(sehirler)
#%%reverse = tersten sıralama
#sehirler.reverse()
#print(sehirler)