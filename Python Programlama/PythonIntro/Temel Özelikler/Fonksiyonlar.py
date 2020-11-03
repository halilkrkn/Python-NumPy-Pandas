# -*- coding: utf-8 -*-

#
#
#def selamVer(isim = "dostum"):
#    print("merhaba "+ isim)
#    
#selamVer()
##selamVer("Halil")    
#
#def selamVer2(isim = "dostum", soyIsim = "ehabah"):
#    print("merhaba "+ isim + soyIsim)
#
#selamVer2("halil"," karkın")    
#
#%%
def dikUcgenAlaniHesapla(a,b):
    return a*b/2

alan = dikUcgenAlaniHesapla(3,7)

print(alan)

#%%
dikUcgenAlaniHesapla2 = lambda a,b: a*b/2

print(dikUcgenAlaniHesapla2(3,6))

print(type(dikUcgenAlaniHesapla2))


x = dikUcgenAlaniHesapla2

print(x(4,5))