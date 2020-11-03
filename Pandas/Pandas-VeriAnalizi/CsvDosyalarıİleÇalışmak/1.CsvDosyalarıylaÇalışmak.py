# -*- coding: utf-8 -*-

import pandas as pd

notlar = pd.read_csv("grades.csv")
notlar.columns= ["İsim","Soyisim","SSN","Test1",
                 "Test2","Test3","Test4",
                 "Final","Sonuç"]
#print(type(df))
print(notlar.head())
print(notlar.tail())

print(notlar)
#print(notlar["SSN"])

print(notlar.iloc[2])

print(notlar[0:10])