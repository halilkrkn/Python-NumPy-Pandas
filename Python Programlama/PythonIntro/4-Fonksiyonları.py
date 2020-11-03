
#FONKSIYONLARA GIRIS VE FONKSIYON OKURYAZARLIGI

print("a","b", sep = "_")
#?print
print()

len("a")


#Matematiksel Islemler

4*4
4/4
5-1
6+3
3**2
3**3


#Fonksiyon Nasil Yazilir?

4**2

def kare_al(x):
    print(x**2)
    
kare_al(5)    

#Bilgi Notuyla Cikti Uretmek

def kare_al(x):
    print(x**2)
    
kare_al(5)  

def kare_al(x):
    print("Girilen Sayinin Karesi:" + str(x**2))

kare_al(3)

def kare_al(x):
    print("Girilen Sayi:" + 
          str(x) + 
          ", Karesi:" +
          str(x**2))

kare_al(3)


#Iki Argumanli Fonksiyon Tanimlamak

def kare_al(x):
    print(x**2)
    
    
def carpma_yap(x, y):
    print(x*y)
    
carpma_yap(2,3)

#On Tanimli Argumanlar

#?print

def carpma_yap(x, y = 1):
    print(x*y)

carpma_yap(3,4)

print("HELLO AI ERA")

#Argumanlarin Siralamasi

def carpma_yap(x, y = 1):
    print(x*y)

carpma_yap(y = 2, x = 3)

carpma_yap(2,3)


#Ne Zaman Fonksiyon Yazilir?

#isi, nem, sarj

(40+25)/90


def direk_hesap(isi, nem, sarj):
    print((isi + nem)/sarj)

direk_hesap(25,40,70)

#Ciktiyi Girdi Olarak Kullanmak

def direk_hesap(isi, nem, sarj):
    print((isi + nem)/sarj)

cikti = direk_hesap(25,40,70)
cikti
print(cikti)
direk_hesap(25,40,70)*9


def direk_hesap(isi, nem, sarj):
    return (isi + nem)/sarj


cikti = direk_hesap(25,40,70)
cikti
print(cikti)
direk_hesap(25,40,70)*9

def direk_hesap(isi, nem, sarj):
    return 
    (isi + nem)/sarj


direk_hesap(25,40,70)


#Local ve Global Degiskenler

x = 10
y = 20

def carpma_yap(x = 2,y = 1):
    return x*y


carpma_yap(2,3)

#Local Etki Alanindan Global Etki Alanini Degistirmek


x = []
#del x

def eleman_ekle(y):
    x.append(y)
    print(str(y) + " ifadesi eklendi")

eleman_ekle("ali")

eleman_ekle("veli")

x
