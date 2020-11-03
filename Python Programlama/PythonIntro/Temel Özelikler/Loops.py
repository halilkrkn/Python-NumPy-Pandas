# -*- coding: utf-8 -*-

#numbers = [6,5,3,8,4,2,5,4,11]
#
#sum = 0
#
#for val in numbers:
#    sum = sum+val
#
#print("the sum is",sum)

sehirler = ["Mersin", "Erzurum", "Rize","Sinop","İstanbul","Niğde"]

#for sehir in sehirler:
#    print(sehir.upper())
#    print(sehir[0])

#%% For intro
for sehir in sehirler:
    if sehir != "Mersin":
        print(sehir + " için kod = " + sehir[0:3])
    print("***********************")   

#%% For Range
for x in range(1,100,2):
    print(x+2)



    