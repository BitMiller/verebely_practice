# @241106-3-2016
# feladat13.py
"""
A bankjegyautomatából az ügyfél legfeljebb 300 000 Ft-ot vehet föl, 1 000, 5 000 és 10 000 Ft-os címletekben.
A program kérjen be egy ezerrel osztható összeget, majd határozza meg, hogy egy beolvasott összeget milyen
címletekben kell kifizetni, ha a lehető legkevesebb bankjegyet akarjuk felhasználni. (bankjegy)
A megoldást a következő formában írja ki:
[...] -> pdf
"""

# Program run command in Android:Termux:Python :
runCmd = "python /storage/emulated/0/BitMiller/Pradhana/Dropbox/bitmiller_hu/verebely_progs/programozasi_alapok/gyakorlo_feladatok/feladatok1_pdf/feladat13.py"

from math import *
#import math

def getinput(s = ""):
 if s != "":
  print(s, end=" : ")
 while True:
  inp = input()
  try:
   inp = int(inp)
  except ValueError:
   print("Integert kérek! ", end="")
  else:
   if inp%1000 != 0:
    print("A szám 1000-vel osztható legyen! ")
   else: break
 return inp


eredeti_osszeg = osszeg = getinput('Adj!')

l = len(str(osszeg))

#print(str(osszeg:=getinput('Adj!'))+f" - ennyi, amit löktél.")

#print(osszeg:=getinput('Adj!')+f" Ennyi, amit löktél: {osszeg}")
# NameError: name 'osszeg' is not defined

#print(f"Ezt lökted: {osszeg:=getinput('Adj!')}")

#print(f"Összeg: {osszeg}")

bjegy_10000 = floor(osszeg/10000)
osszeg = osszeg-bjegy_10000*10000
bjegy_5000 = floor(osszeg/5000)
osszeg = osszeg-bjegy_5000*5000
bjegy_1000 = floor(osszeg/1000)

tab = 0
if tab<len(str(bjegy_10000)): tab=len(str(bjegy_10000))
if tab<len(str(bjegy_5000)): tab=len(str(bjegy_5000))
if tab<len(str(bjegy_1000)): tab=len(str(bjegy_1000))

#print(f"tab = {tab} ; l = {l}")

s = f"{str(bjegy_10000):>{tab}} * 10000 = {str(bjegy_10000*10000):>{l}}"
print(s)
print(f"{str(bjegy_5000):>{tab}} *  5000 = {str(bjegy_5000*5000):>{l}}")
print(f"{str(bjegy_1000):>{tab}} *  1000 = {str(bjegy_1000*1000):>{l}}")

for _ in range(len(s)):
 print("_", end="")

print(f"\nÖsszeg:{eredeti_osszeg:>{len(s)-7}} Ft");




