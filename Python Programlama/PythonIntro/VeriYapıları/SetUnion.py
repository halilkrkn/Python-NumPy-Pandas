# -*- coding: utf-8 -*-


setA = {1,3,4,5}
setB = {1,2,3,4,5,7,8,9,6}

print(setA | setB)
print(setA.union(setB))

print(setA & setB)
print(setA.intersection(setB))

print(setB- setA)
print(setB.difference(setA))

print(setA ^ setB)
print(setA.symmetric_difference(setB))



#Set Sorgu İşlemleri

set1 = set([7,8,9])
set2 = set([5,6,7,8,9,10])

# İki kümenin kesişiminin boş olup olmadığının sorgulanması

isdisjoint = set1.isdisjoint(set2)
print(isdisjoint)

# Bir kümenin bütün elemanlarının baska bir kume içerisinde yer alıp almadığı
issubset = set1.issubset(set2)
print(issubset)
#Bir kümenin bir diğer kumeyi kapsayıp kapsamadığı

issuperset = set2.issuperset(set1)
print(issuperset)

