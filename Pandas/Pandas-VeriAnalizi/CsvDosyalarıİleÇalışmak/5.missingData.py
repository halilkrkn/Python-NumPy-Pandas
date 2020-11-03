# -*- coding: utf-8 -*-

import pandas as pd

url = 'https://raw.githubusercontent.com/justmarkham/DAT8/master/data/ufo.csv'

data = pd.read_csv(url)

print(data[["City",
            "Colors Reported",
            "Shape Reported",
            "State",
            "Time"]].head())
print(data.columns)
# verimizde null olan var mı dedik ve null olanları getirdik.
print(data.isnull().head(100))
print("*************************")
#verimizde null olmayanları getirdik.
print(data.notnull().head(100))
print("*************************")
#
print(data.isnull().sum())
print("*************************")
print(data[data.City.isnull()])

#dropna() fonk. ile verilerimiz içerisinde gereksiz uyumsuzları çıkarıyoruz.
# Yani dropna() fonk. u bozuk dataları çıkarıyor örn. NaN olan verileri.
#print(data.shape)

#data = data.dropna(how="any")
#
#print(data.shape)
#
#data = data.dropna(
#          subset=['City','Colors Reported'],how="all")
#
#print(data.shape)

# fillna() ile Nan olan kısımlara Belirsiz olarak belirtiyoruz.

data['Colors Reported'].fillna(value ='Belirsiz', inplace=True)
print(data['Colors Reported'].value_counts(dropna=False))
print(data)

