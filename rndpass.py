import sys
from random import *

karakter = "abcdefghijklmnoprstuvyzwxABCDEFGHIJKLMNOPQRSTUVWXYZ"
sayi = "0123456789"
ozel = "'!#@.,$"

answer = input("Parolanın içerisinde sayı olsun mu? [E/H]")
if answer == "E":
    print("Sayi eklendi.")
elif answer == "H":
    print("Sayi eklenmedi.")

answer2 = input("Parolanın içerisinde harf olsun mu? [E/H]")
if answer2 == "E":
    print("Harf eklendi.")
elif answer2 == "H":
    print("Harf eklenmedi.")

answer3 = input("Parolanın içerisinde ozel karakter olsun mu? [E/H]")
if answer3 == "E":
    print("Ozel karakter eklendi.")
elif answer3 == "H":
    print("Ozel karakter eklenmedi.")

if answer == "E" and answer2 == "E" and answer3 == "E":
    hepsi = sayi + karakter + ozel
if answer == "E" and answer2 == "E" and answer3 == "H":
    hepsi = sayi + karakter
if answer == "E" and answer2 == "H" and answer3 == "E":
    hepsi = sayi + ozel
if answer == "E" and answer2 == "H" and answer3 == "H":
    hepsi = sayi
if answer == "H" and answer2 == "E" and answer3 == "E":
    hepsi = karakter + ozel
if answer == "H" and answer2 == "E" and answer3 == "H":
    hepsi = karakter
if answer == "H" and answer2 == "H" and answer3 == "E":
    hepsi = ozel
if answer == "H" and answer2 == "H" and answer3 == "H":
    print("Lutfen bir girdi seciniz.")
    sys.exit()
min = int(input("Min:"))
max = int(input("Max:"))
sifre ="".join(choice(hepsi) for x in range(randint(min, max)))
print("Sifreniz =",sifre)
