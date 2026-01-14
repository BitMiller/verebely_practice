# @241119-2-1655
# feladat14.pdf

"""
Kérjünk be egy szót és cseréljük le benne a magyar ékezetes betűket az angol ábécé megfelelő ékezet nélküli betűire.
"""

# Program run command in Android:Termux:Python :
runCmd = "python /storage/emulated/0/BitMiller/Pradhana/Dropbox/bitmiller_hu/verebely_progs/programozasi_alapok/gyakorlo_feladatok/feladatok4_pdf/feladat14.py"

ekezetek = {
 "á" : "a",
 "é" : "e",
 "í" : "i",
 "ó" : "o",
 "ö" : "o",
 "ő" : "o",
 "ú" : "u",
 "ü" : "u",
 "ű" : "u",
 "Á" : "A",
 "É" : "E",
 "Í" : "I",
 "Ó" : "O",
 "Ö" : "O",
 "Ő" : "O",
 "Ú" : "U",
 "Ü" : "U",
 "Ű" : "U",
}

s = input("Ékezetes szöveg ide: ")

s2:str = ""

for c in s:
 if c in ekezetek:
  s2 += ekezetek[c]
 else: s2 += c

print(f"Eredmény: {s2}")

