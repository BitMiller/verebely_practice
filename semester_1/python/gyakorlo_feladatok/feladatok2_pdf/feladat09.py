# @241119-2-1655
# feladat09.pdf

"""
Írassuk ki a képernyőre a 100-nál nem nagyobb páratlan számokat! (paratlan)
"""

# Program run command in Android:Termux:Python :
runCmd = "python /storage/emulated/0/BitMiller/Pradhana/Dropbox/bitmiller_hu/verebely_progs/programozasi_alapok/gyakorlo_feladatok/feladatok2_pdf/feladat09.py"

szamok:list[int] = []

for i in range(101) :
 if i%2==1 : szamok.append(i)

print(f"Ímhol a 100-nál nem nagyobb páratlan számok, e! : {szamok}")
