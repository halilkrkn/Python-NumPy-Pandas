# -*- coding: utf-8 -*-

# sys kütüphanesi bir hatanın hangi hata olduğunu anlamak için kullanılır.

import sys

liste = [7,'halil',0,3,"6"]

for x in liste:
    print("\n")
    try:
        print("Sayı: "+ str(x))
        sonuc = 1/int(x)
        print("Sonuç: "+ str(sonuc))
 
    except ValueError:
        print(str(x)+ " bir sayı değildır")
    except ZeroDivisionError:
        print(str(x)+ " Sıfıra Bölme Hatasıdır")
        
    except:
        print(str(x)+" hesaplanamadı")
        print("Sistem Diyor ki: "+ str(sys.exc_info()[0]) + " Hatasıdır bu")
    finally:
        print("İşlemler Bitti")