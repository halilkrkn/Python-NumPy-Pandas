# -*- coding: utf-8 -*-

import numpy as np

# indeksleme bir dizinin istenilen indeksine ulaşma.

sayilar = np.array([0,5,10,15,20,25,30])

# Tersten dizilim yaptık.
print(sayilar[::-1])

# 0. index ten 2. index e kadar 
#Çıktı : [ 0  5 10]

#print(sayilar[0:3])

sayilar2 = np.array([[0,5,10],[15,20,25]])

#print(sayilar2)

#print(sayilar2[:,0:2])

#print(sayilar2[-1,:])

print(sayilar2[:,-1])