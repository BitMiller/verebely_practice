# @241119-2-1655
# feladat13.pdf

"""
Számoljuk meg egy szóban a magánhangzókat!
"""

# Program run command in Android:Termux:Python :
runCmd = "python /storage/emulated/0/BitMiller/Pradhana/Dropbox/bitmiller_hu/verebely_progs/programozasi_alapok/gyakorlo_feladatok/feladatok4_pdf/feladat13.py"

s = input("Jöhet a szöveg! : ")

mghk = "aáeéiíoóöőuúüű"

db:int = 0

for c in s:
 if c in mghk:
  db+=1

print(f"Ennyi a mgh: {db}")

