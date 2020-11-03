# -*- coding: utf-8 -*-

#Join = iki farklı datanın belli kriterlere göre bir araya getirilmesidir.

import pandas as pd

data1 = {
         
         'id':[1,2,3,4],
         'ad':["Halil","Göktug","Belkız", "Betül"],
         'soyad':["Karkın","Karkın","Çolak","Er"]             
         
         }

data2 = {
         
         'id':[1,3,4,7],
         'ad':["ElifGül","Yusuf","Musa", "Seda"],
         'soyad':["Çolak","Er","Karkın","Özturhan"]             
         
         }

## data1 ve data2 yi data frame çeviriyoruz.

data1Df = pd.DataFrame(data1)
data2Df = pd.DataFrame(data2)

print(data1Df)
print("*************************")
print(data2Df)
print("************************")

## Join yapıyoruz burda merge sayesinde 
## Yani burda id si aynı olanları yan yana getirdik. 
## yani burda innerJoin Yapmış olduk how ile onu belirttik.
## Yani innerJoin ile Aynı İd ye ait olanları listeledik.
print(pd.merge(data1Df,data2Df,on='id', how ="inner"))
print("************************")
## LeftJoin yaptık = solda olup sağda olmayanlarıda listeliyoruz.
print(pd.merge(data1Df,data2Df,on='id', how ="left"))
print("************************")
## LeftJoin yaptık = sağda olup solda olmayanlarıda listeliyoruz.
print(pd.merge(data1Df,data2Df,on='id', how ="right"))
print("************************")

print(pd.concat([data1Df,data2Df], axis=1))






























