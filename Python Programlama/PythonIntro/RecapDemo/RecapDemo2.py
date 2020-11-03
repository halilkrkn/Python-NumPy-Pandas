# -*- coding: utf-8 -*-

ogrenciler= ["halil","fatih","berkay","Samil","Melih"]

fileToAppend = open("ogrenciler.txt","a")

for ogrenci in ogrenciler:
    fileToAppend.write(ogrenci)
    fileToAppend.write("\n")
fileToAppend.close()