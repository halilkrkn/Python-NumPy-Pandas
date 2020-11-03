#SAYILAR VE STRINGLERE GIRIS
9
9.2
9+9
9*9

print('HELLO AI ERA')
"HELLO AI ERA"

type(9)
type(9.2)
type("HELLO AI ERA")

#STRINGLERE YAKINDAN BAKALIM

""
''

123
type(123)
"123"
type("123")

"a" + "b" 
"a" " b" 
"a" + "-b" 

"a" - "b" 

"a "*3
"a"/3

#STRING METODLARI - len()

gel_yaz = "gelecegi_yazanlar"
#del mvk

a = 9
b = 10

a*b


len(gel_yaz)
len("gelecegi_yazanlar")

#STRING METODLARI - upper() & lower()

gel_yaz = "gelecegi_yazanlar"

gel_yaz.upper()
gel_yaz.lower()

gel_yaz.islower()
B = gel_yaz.upper()

B.islower()
B.isupper()

#STRING METODLARI - replace()

gel_yaz = "gelecegi_yazanlar"

gel_yaz.replace("e","a")

gel_yaz.replace("a","i")

#STRING METODLARI - strip()

gel_yaz = " gelecegi_yazanlar "
gel_yaz.strip()

gel_yaz = "*gelecegi_yazanlar*"
gel_yaz.strip("*")

gel_yaz = "lgelecegi_yazanlarl"
gel_yaz.strip("l")

#METODLARA GENEL BAKIS

gel_yaz = "gelecegi_yazanlar"

dir(gel_yaz)

gel_yaz.capitalize()
gel_yaz.title() 


#SUBSTRINGLER

gel_yaz = "gelecegi_yazanlar"

gel_yaz[1]

gel_yaz[20]

gel_yaz[0:3]

#DEGISKENLER

a = 9
b = "ali_uzaya_git"
c = a*2


a/c
a*c
a*5

type(100)
type(100.2)
type(1+2j)

a = 100.2

#TYPE_DONUSUMLERI

toplama_bir = input()
toplama_iki = input()

type(toplama_bir)

toplama_bir + toplama_iki

int(toplama_bir) + int(toplama_iki)

int(11.0)

12

float(12)

type(str(12))

#print()

print("HELLO AI ERA")

print("gelecegi","yazanlar")

print("gelecegi","yazanlar", sep = "_")

print()

type()

print()
