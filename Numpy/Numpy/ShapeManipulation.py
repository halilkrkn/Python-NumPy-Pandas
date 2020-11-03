# -*- coding: utf-8 -*-
import numpy as np

a = np.floor(10*np.random.random((3,4)))

print(a)

# hangi formatta matris olduğunu gösteriyor.
#Çıktı: (3,4)
print(a.shape)
# tek boyuta çevirdi.
print(a.ravel())

a = a.ravel()

print(a)

print(a.shape)

a = a.reshape(2,6)
print(a)
print(a.T) # transpozunu aldık.
print(a.reshape(2,-1))

