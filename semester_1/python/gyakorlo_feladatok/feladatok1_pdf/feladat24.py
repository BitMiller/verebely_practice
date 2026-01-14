# @241106-3-2016
# feladat24.py
"""
Írj programot, amely bekér a felhasználótól egy helységnevet, valamint ennek a helységnek a lélekszámát, és a megadott lélekszámtól függően kiírja, hogy az adott helység milyen településtípusba tartozik. (telepules)
 ha a lélekszám kevesebb, mint 5000, akkor község
 ha a lélekszám legalább 5000, de kevesebb, mint 20 000, akkor kisváros
 ha a lélekszám legalább 20 000, de kevesebb, mint 100 000, akkor középváros
 ha a lélekszám legalább 100 000, de kevesebb, mint 1 000 000, akkor nagyváros
 ha a lélekszám legalább 1 000 000, akkor metropolis
 ha a felhasználó 0 vagy annál kisebb számot ad meg, a program írja ki, hogy "Hibás adatbevitel"
"""

# Program run command in Android:Termux:Python :
runCmd = "python /storage/emulated/0/BitMiller/Pradhana/Dropbox/bitmiller_hu/verebely_progs/programozasi_alapok/gyakorlo_feladatok/feladatok1_pdf/feladat24.py"


class Telepules:
 def __init__(self, elnevezes, tol):
  self.elnevezes = elnevezes
  self.tol = tol


fajta = []

fajta.append(Telepules("község", 0))
fajta.append(Telepules("kisváros", 5000))
fajta.append(Telepules("középváros", 20000))
fajta.append(Telepules("nagyváros", 100000))
fajta.append(Telepules("metropolisz", 1000000))


print(len(fajta))


nev = input("Melyik településről meséljek? : ")
lakos = float(input("Lélekszám? (Remélem, egész...) : "))

if lakos==0: print("Hibás adatbevitel!")
elif lakos<0:
 print(f"Bukó, mert a(z) {lakos} negatív szám. Túlteljesítették a komcsik a kitelepítést, vagy mi?")
else:
 for i in range(1, len(fajta)):
  if lakos<fajta[i].tol:
   print(f"Márpedig ez a(z) {nev} település {fajta[i-1].elnevezes} településtípusú!")
   break
  elif i==len(fajta)-1:
   print("Bingóóó! Me-me-me-metropolisz - isz - isz - isz...!")




