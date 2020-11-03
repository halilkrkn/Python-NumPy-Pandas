# -*- coding: utf-8 -*-

# r read
# a apend = hem okuma hem yazma ekleme
# w write
# x create
#xt = text dosyası olarak oluşturur
#xb = binary dosyası olarak oluşturur.
#read() = tamamını okuyor
#readLine()= Satır satır okuyor


f = open("musteriler.txt")
#ff= f.read()
#print(ff)
#%%
#print("*********")
#print(f.readline())
#print(f.readline())
#%%
for l in f: # dosyadaki bütün Lineları geziyor okuyor
    print(l)
    
f.close()
 #%% append ve write kullanımı
fileToAppend = open("ogrenciler.txt","w")

fileToAppend.write("\n")
fileToAppend.write("En iyi Takımıdır")
fileToAppend.close()
#%%
import os 

if os.path.exists("ogrenciler.txt"):
    os.remove("ogrenciler.txt")
else:
    print("böyle bir dosya yok")

os.rmdir("empty") # Boş dosyayı silmek için
