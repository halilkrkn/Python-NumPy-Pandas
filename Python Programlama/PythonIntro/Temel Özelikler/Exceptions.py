# -*- coding: utf-8 -*-

try:
    sayi = int(input("Sayi Giriniz: "))
except ValueError:  # eğer valueError alursam anlamında dır böyle olursa
        print("Tip UyuşMazlığı : Lütefen Sayı giriniz")
except (ValueError,ZeroDivisionError):# Bu iki Hata varsa bu kısmı yap demek.
    print("Payda Sıfır Olamaz")
except:
    print("Bir Hata Oluştu")

print("bitti")

