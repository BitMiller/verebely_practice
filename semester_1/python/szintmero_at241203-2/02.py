# @241203-2-1839
# Program run command in Android:Termux:Python :
runCmd = "python /storage/emulated/0/BitMiller/Pradhana/Dropbox/bitmiller_hu/verebely_progs/programozasi_alapok/szintmero_at241203-2/02.py"


from math import *

igen = ["igen", "i", "1"]
nem = ["nem", "n", "0"]
aruk = [
 {"nev" : "paradicsom", "szam" : "1", "ar" : 1199},
 {"nev" : "paprika", "szam" : "2", "ar" : 1349},
 {"nev" : "vöröshagyma", "szam" : "3", "ar" : 289},
]
vegosszeg:int = 0

def aru_valasztas(aru):
 global aruk
 letezik = 0
 for a in aruk:
  if aru.lower()==a["nev"] or aru==a["szam"]:
   letezik = int(a["szam"])
   break
 return letezik

def get_float():
 while True:
  f = input()
  try:
   f_num = float(f)
  except ValueError:
   print("Kérem, számot adjon meg! : ")
  else: break
 return f_num

print("Üdv a piacon!\nSúgó:\nIgen = igen / i / 1\nNem = nem / n / 0\nTermék neve lehet a termék sorszáma is.")
print("Íme a termékek és áraik:")
for e in aruk:
 print(f"({e["szam"]}) {e["nev"]}: {e["ar"]:>{15-len(e["nev"])}} Ft/Kg")

while True:
 print("Kíván valamit vásárolni? : ", end="")
 while True:
  valasz = input()
  print(f"Debug: {valasz.lower}")
  if valasz.lower() in igen or valasz.lower() in nem: break
  else: print("Neméétem. Hogymondgya? : ", end="")
 if valasz.lower() in nem: break
 print("Noés mit?\n1: Paradicsom\n2: Paprika\n3: Vöröshagyma")
 while True:
  valasz = input()
  valasztott_aru = aru_valasztas(valasz)
  if valasztott_aru == 0:
   print("Na most akkor mi van? : ", end="")
  else:
   print(f"És hány kilogrammot kér a {aruk[valasztott_aru-1]["nev"]}-ból? : ", end="")
   mennyiseg = get_float()
   vegosszeg += round(aruk[valasztott_aru-1]["ar"]*mennyiseg)
   break

print(f"A végösszeg: {vegosszeg}\nKöszönjük, hogy a piacon vásárolt!")
