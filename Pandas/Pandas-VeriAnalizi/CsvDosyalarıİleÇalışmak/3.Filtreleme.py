# -*- coding: utf-8 -*-

import pandas as pd
films = pd.read_csv("imdb_1000.csv")
print(films)
#columns bilgilerini gösterdik
print(films.columns)
#%% İlk 5 kayıt
print(films.head())
#%% Son 5 kayıt
print(films.tail())
#%% filmlerin isimlerini aldık
print(films.title.head())
#print(films["title"].head()) yukardaki ile aynı anlamda.
print("****************************************")
print(films[["title","star_rating"]].head())
print("****************************************")
print(films[:6][["title","star_rating"]].head(10))

#%% Filtreleme yaptık [(films['star_rating']>=8.5)&(films['star_rating'] bu kısım filreleme
print(
      films[(films['star_rating']>=8.5)&(films['star_rating']<=9.0)]
[["title","star_rating"]])
#%% Filtreleme yaptık [(films['star_rating']>=8.5)|(films['star_rating'] bu kısım filreleme
print(
      films[(films['star_rating']>=8.5)|(films['star_rating']<=9.0)]
[["title","star_rating"]])
#%% Query İle filtreleme İşlemleri yaptık

print(films.query("star_rating >= 9.0 & star_rating <=9.2"))
print("****************************************")
print(films.query("star_rating >= 9.0 | star_rating <=7.4"))