# -*- coding: utf-8 -*-

import pandas as pd 

films = pd.read_csv("imdb_1000.csv")

print(films.columns)
print("*******************************")
#İstemediğimiz alanı drop() fonk. ile çıkarabiliyoruz dosyadan.
# burda sütun(kolon) olduğunu belirtmek için axis = 1 diyoruz.

films = films.drop('content_rating',axis=1)

#Ama satır old. belirtmek için ise axis = 0 ı kullanıyoruz.
# Ve satırları istenilen formatta silmiş oluyoruz.
# mesela burda 2. satırı sildik

# 2. satırı silmiş olduk.
films = films.drop(2,axis=0)

rowToDrop = [0,1,6,4,5,6,7,8]
films = films.drop(rowToDrop,axis=0)
print(films.mean())
 
#print(films.drop("content_rating",axis=1).head().columns) #Kaç columns kaldığını gösterdik.
print("*******************************")

