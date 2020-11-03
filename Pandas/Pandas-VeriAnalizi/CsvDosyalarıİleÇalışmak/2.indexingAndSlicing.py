# -*- coding: utf-8 -*-

import pandas as pd

notlar = pd.read_csv("2.2 grades.csv")
notlar.columns= ["İsim","Soyisim","SSN","Test1",
                 "Test2","Test3","Test4",
                 "Final","Sonuç"]
print(notlar)

#%%bu şekilde tüm isimleri aldık.
print(notlar.loc[:,"İsim"])
print("************")
#%%İlk 5 İsmi aldık.
print(notlar.loc[:5,"İsim"])
print("************")
#%% İsimden Test3 e kadar ki olan kısmı aldık ve 5 ilk 5 kişiyi gösterdik.
print(notlar.loc[:5,"İsim":"Test3"])
print("************")
#%% isim ve Final notlarını gösterdik.
print(notlar.loc[:5,["İsim","Soyisim","Final"]])
print("************")

#%% En baştan test3 e kadar ki her şeyi almış oldu.
print(notlar.loc[:5,:"est3"])
print("************")

#%% Tersten 1 er 1 er sıralama
print(notlar.loc[::-1,:"Soyisim"])
print("************")
#%% Tersten 5 er 5 er sıralama
print(notlar.loc[::-5,:"Soyisim"])
print("************")
#%% Normal 2 ser 2 ser sıralama
print(notlar.loc[::2,:"Soyisim"])