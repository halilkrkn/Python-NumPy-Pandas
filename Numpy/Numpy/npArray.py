# -*- coding: utf-8 -*-

import numpy as np

#burada 1 i koyarak başlangıcı belirledik. Yani 1 den başlayacak.
#a = np.arange(1,10)

a = np.array([1,2,3,4,5,6,7,8,9])

#print(str(a) + str(a.dtype)+" hepsini int olarak gördü")

a= a.reshape(1,9)

print(str(a)+" "+str(a.ndim) + " boyutludur.\n" )

#b = np.array([1.9,2,3,4,5,6])
#print(str(b) +str(b.dtype)+ " hepsini float olarak gördü")
#
#
#c = np.array(["1",2,3,4,5,6])
#print(str(c) +str(c.dtype)+ " hepsini string olarak gördü")
#


b = np.array([[7,8],[3,5],[1,2]])

b = b.reshape(2,3)

print(str(b)+" "+str(b.ndim) + " boyutludur." )
b= b