# @241105-2-1930
# feladat05.py
"""
5. Írjunk programot, amely bekéri egy téglalap oldalait, és kiszámolja a kerületét és területét!
(teglalap_ker_ter)
"""

# Program run command in Android:Termux:Python :
runCmd = "python /storage/emulated/0/BitMiller/Pradhana/Dropbox/bitmiller_hu/verebely_progs/programozasi_alapok/gyakorlo_feladatok/feladatok1_pdf/feladat05.py"


import re


print("Accsak a téglalapod 2 oldala hosszát! (kettő számot adgyá') : ")
oldalak = input()

szamok = list(map(int, re.findall(r"\d+", oldalak)))

#print(type(szamok))

print(f"Ezek az oldalhosszok: {szamok}")
#print(i, sep=" ") for i in szamok:
#print(", ".join(map(str, szamok)))

print(f"Íme a kerület: {(szamok[0]+szamok[1])*2} egység")
print(f"Íme a terület: {szamok[0]*szamok[1]} egység^2")

"""
s = ","
print(s.join(("a","b")))
print(s.join(("a,b")))
"""






