# @241119-2-1655
# feladat06.pdf

"""
Kérjünk be egy tetszőleges szöveget, és számoljuk meg, hogy hány "e" betű van benne!
"""

# Program run command in Android:Termux:Python :
runCmd = "python /storage/emulated/0/BitMiller/Pradhana/Dropbox/bitmiller_hu/verebely_progs/programozasi_alapok/gyakorlo_feladatok/feladatok4_pdf/feladat06.py"


szoveg = input("Acca szöveg : ")

e_betuk:int = 0

for c in szoveg:
 if c == "e":
  e_betuk += 1

print(f"{e_betuk}db \"e\" betű van a \"{szoveg}\" szóban.")


