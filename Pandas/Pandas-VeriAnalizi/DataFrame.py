# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np

# dataFrame de index(satırı) ve coloum(sütun) larla çalışabiliyoruz.
data = [10,20,30,40,50]
df = pd.DataFrame(data)
print(df)
print("******************")


# burda columns kullanarak excel formatına çevirdik bir nevi satır sütun şeklinde yapmış olduk.
data2 = [["Halil",24,"Osmaniye"],["Musa",34,"Osmaniye"],["Yusuf",5,"İstanbul"]]
df2 = pd.DataFrame(data2, columns=["İsim","Yaş","Şehir"], index= [1,2,3])
print(df2)
#print(df2["Yaş"])

print("******************")

# Sözlük ile de yaptık.
data3 = {"İsim":["Halil","Musa","Goktug"],
         "Yaş":[24,34,5],
         "Şehir": ["Sakarya","Osmaniye","İstanbul"]}
df3 = pd.DataFrame(data3, columns=["İsim","Yaş","Şehir"], 
                   index= [1,2,3])
print(df3["İsim"])

# burda del ile şehir kolonunu silmiş olduk.
#del df3["Şehir"]
#df3.pop("Şehir") # del komutu ile aynı işi görüyor.
print(df3)
print("*************")

# burada 2 numaralı columns un bilgilerini getirdik.
print(df3.loc[2])
print("*************")
print(df3.iloc[2])

print("************")
# burada df2 nin bilgilerini de df3 le beraber gösterdik.
df4 = df3.append(df2)
print(df4)

print("************")

# Baştaki datayı görmek için kullandık.
print(df4.head(3))
print("************")
# Sondaki datayı görmek için kullandık.
print(df4.tail(2))
