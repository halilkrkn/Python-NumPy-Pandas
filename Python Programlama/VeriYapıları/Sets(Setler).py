# -*- coding: utf-8 -*-

# Set = Setlerde listedeki var olan bir datayı değiştiremiyoruz. 
## Ama listeye yeni bir eleman eklenir.
# Setler - Sets

#- Sırasızdır.
#- Değerleri Eşsizdir.
#- Değiştirelebilirdir.
#- Farklı Tipleri Barındırabilir.

#- a= {} ve set([]) içerisine verileri yazarak yaparız.


studentsSet = {"Halil", "Göktuğ","Yusuf","Musa"}
print(studentsSet)

for student in studentsSet:
    print(student)
    
print("Halil" in studentsSet)    

if "Halil" in studentsSet:
    print("listede Var")

studentsSet.add("ELifgÜl")
print(studentsSet)

studentsSet.update(["Hatice", "Belkız", "Betül"])
print(studentsSet)

print(len(studentsSet))

studentsSet.remove("Halil")
print(len(studentsSet))

studentsSet.discard("Halil") ## Sildiğinde hata vermiyor
print(len(studentsSet))

x = studentsSet.pop()
print(len(studentsSet))
print(studentsSet)

x= studentsSet.clear()
print(len(studentsSet))
del studentsSet
#print(studentsSet)