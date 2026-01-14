# @241119-2-1655
# feladat17.pdf

"""
Kérjen be a felhasználótól két szót, és döntse el, hogy a két szó anagramma-e! Ha azok voltak, írja ki a képernyőre az „Anagramma” szót, ha nem, akkor pedig a „Nem anagramma” szöveget!
"""

# Program run command in Android:Termux:Python :
runCmd = "python /storage/emulated/0/BitMiller/Pradhana/Dropbox/bitmiller_hu/verebely_progs/programozasi_alapok/gyakorlo_feladatok/feladatok4_pdf/feladat17.py"

szo1 = input("Első szó: ")
szo2 = input("Második szó: ")

l1 = []
l2 = []

for c in szo1.lower():
 l1.append(ord(c))

l1.sort()

for c in szo2.lower():
 l2.append(ord(c))

l2.sort()

if l1==l2:
 print("Anagramma!")
else:
 print("Ana nem gramma!")
