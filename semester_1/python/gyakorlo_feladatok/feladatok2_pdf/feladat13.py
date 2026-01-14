# @241119-2-1655
# feladat13.pdf

"""
Kérjük be a felhasználótól egy számtani sorozat két szomszédos tagját. A program írja ki a sorozat előző és következő 10 tagját! (szamtanisor3)
"""

# Program run command in Android:Termux:Python :
runCmd = "python /storage/emulated/0/BitMiller/Pradhana/Dropbox/bitmiller_hu/verebely_progs/programozasi_alapok/gyakorlo_feladatok/feladatok2_pdf/feladat13.py"

elso_tag = int(input("Kérem az első tagot: "))
masodik_tag = int(input("Kérem a második tagot: "))

difi = masodik_tag - elso_tag

szamok:list[int] = []

for i in range(1,11) :
 szamok.append(elso_tag-difi*i)

print(f"Előző 10 tag: {szamok}")


szamok:list[int] = []

for i in range(0,10) :
 szamok.append(masodik_tag+difi*i)

print(f"Következő 10 tag: {szamok}")