# -*- coding: utf-8 -*-

"""
@halilkrkn
#"""
#sayi*sayi = sayi**2 
sayilar = [1,2,3,4,5]

sayilarinKaresi = list(map(lambda x: x**2,sayilar))

#for sayi in sayilar:
#    sayilarinKaresi.append(sayi*sayi)
    
sayilarfiltreli = list(filter(lambda sayi: sayi>2,sayilar))
print(sayilar)
print(sayilarinKaresi)
print(sayilarfiltreli)

from functools import reduce
sayilarFaktoriyel = reduce(lambda x,y:x*y,sayilar)
print("\n"+ str(sayilarFaktoriyel))