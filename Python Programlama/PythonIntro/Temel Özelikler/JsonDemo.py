# -*- coding: utf-8 -*-
# json dosyasını with open ile okuyup sonra kendiliğinden kapancaktır
import json as jsn

#json datayı okuduk.
with open("Users.json") as users:
    data = jsn.load(users)

    for x in range(2):
        print("\n")
        print(data[x]["username"])
        print(data[x]["email"])
        print(data[x]["address"]["street"])
        print(data[x]["address"]["geo"]["lat"])