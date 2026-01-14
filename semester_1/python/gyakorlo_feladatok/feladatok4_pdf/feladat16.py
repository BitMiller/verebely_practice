# @241119-2-1655
# feladat16.pdf

"""
Kérjünk be egy szót, és rendezzük ábécé sorrendbe a karaktereit!
"""

# Program run command in Android:Termux:Python :
runCmd = "python /storage/emulated/0/BitMiller/Pradhana/Dropbox/bitmiller_hu/verebely_progs/programozasi_alapok/gyakorlo_feladatok/feladatok4_pdf/feladat16.py"

s1 = input("Szöveget befelé: ")

l1 = []

for c in s1:
 l1.append(ord(c))

l1.sort()
s2 = ""

"""
for n in l1:
 s2 += chr(n)
"""

s2 = l1
"".join()
print(s2)

#befejezni a végére írt másik változatot, a join-os egyesítést!