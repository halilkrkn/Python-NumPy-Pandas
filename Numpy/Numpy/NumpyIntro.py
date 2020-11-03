 # -*- coding: utf-8 -*-

import numpy as np

#havaDurumu = [[12,21,31],[6,13,24],[32,5,34]]
#print(havaDurumu)

#reshape() ile 35 lik matris oluşturduk
#3 satır , 5 sütun oluyor

a = np.arange(15).reshape(3,5)
print("\n"+ str(a))
#print(str(type(a)))
print("Boyut Sayısı = "+str(a.ndim) + " boyutludur\n")

b = np.arange(10)
print(b)
print(b.shape)