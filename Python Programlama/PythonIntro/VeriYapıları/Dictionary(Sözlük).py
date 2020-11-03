

#Dictionary - Sözlük
#
#- Kapsayıcıdır.
#- SIRASIZDIR.
#- Değiştirelebilirdir.

#{} ile içerisine  key-value değerler şeklinde doldurulur.

#Sözlük Oluşturma

sozluk = { "REG": "Regresyon Modeli",
           "LOJ": "Lojistik Regresyon",
           "CART": "Classification and Reg"
          }

sozluk


#Sozluk Eleman İşlemleri

sozluk["REG"]
#çikti: 'Regresyon Modeli'

#ekleme
sozluk["GBM"] = "Gradient Bossting Mac"
sozluk

#değiştirme
sozluk["REG"] = "Coklu Doğrusal Regresyon"
sozluk



sozluk = {

        "book": "kitap",
        "table":"masa"

}

sozluk2 = dict(kitap = "book", masa="table")
print(sozluk2)

sozluk["book"] = "kitap 1"
sozluk["pencil"] = "kalem"
#del(sozluk["book"])
print(sozluk)