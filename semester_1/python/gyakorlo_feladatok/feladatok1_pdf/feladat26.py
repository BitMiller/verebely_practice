# @241106-3-2016
# feladat26.py
"""
Kérjük be egy diák matematika év végi jegyét numerikus formában, és írjuk ki azt szövegesen
(elégtelen, elégséges, közepes, jó, jeles). Amennyiben a beírt érdemjegy nem 1..5 közötti szám,
úgy a hibás adat kiírás jelenjen meg. (osztalyzat)
"""

# Program run command in Android:Termux:Python :
runCmd = "python /storage/emulated/0/BitMiller/Pradhana/Dropbox/bitmiller_hu/verebely_progs/programozasi_alapok/gyakorlo_feladatok/feladatok1_pdf/feladat26.py"


class jegy_nev:
 def __init__(self, jegy, nev):
  self.jegy = jegy
  self.nev = nev

jegyek = []
jegyek.append(jegy_nev("1", "elégtelen"))
jegyek.append(jegy_nev("2", "elégséges"))
jegyek.append(jegy_nev("3", "közepes"))
jegyek.append(jegy_nev("4", "jó"))
jegyek.append(jegy_nev("5", "jeles"))

erdemjegy = input("Hoci matekjegy : ")

jegy_talalat = -1

for i in range(len(jegyek)):
 if jegyek[i].jegy == erdemjegy:
  jegy_talalat = i
  break;

if jegy_talalat==-1:
 print("Gondold már meg, miket írsz!")
else:
 print(f"Ahá! Szóval a kapott érdemjegy szép magyarul mondva: {jegyek[jegy_talalat].nev}")



