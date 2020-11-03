# -*- coding: utf-8 -*-

import numpy as np


a = np.array([20,30,40,50])

# arange() fonk u 0 dan 3 e kadar array oluşturuyor.
#Çıktı: 0,1,2,3
b = np.arange(4)

c = a-b
# a**2 = ile a nın karesini almış olduk
# Çıktı: 0,1,4,9,


e = 10*np.sin(a)

#print(e<7)
#print(a*b) # elementwise product

# a@b ile @ opeatörünü kullanarak a ve b matrisini çarpmış olduk. 
#Çıktı Sonuç: 260
print(a@b) 

#Matris çarpımının bir diğer gösterimi.
#Çıktı: 260
print(a.dot(b))

# np.ones() fonksiyonu ile birim matris yapabilirsin.
# Çıktı:
#     array([[1., 1., 1.],
#       [1., 1., 1.],
#      [1., 1., 1.]])
# 3x3 matrisinde birim matris oluşturdum.
f = np.ones((3,3))
# np.zeros() fonk. ile 0 (sıfır) matrisi yapabiliriz.
#Çıktı:
#    array([[0., 0., 0., 0.],
#       [0., 0., 0., 0.]])
# 2x3 matrisinde sıfır matrisi oluşturdum.
g = np.zeros((2,4))
# 2x4 matrisini 0 ile 1 arasında random sayılar atadım.
h = np.random.random((2,4))

i = np.sum(a)

j = np.min(b)

k = np.max(b)

l = np.sqrt(b)
