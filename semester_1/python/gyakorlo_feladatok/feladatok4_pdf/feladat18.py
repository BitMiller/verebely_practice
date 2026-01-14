# @241119-2-1655
# feladat18.pdf

"""
Generáljunk 8 karakteres véletlen-jelszót az alábbi karakterek felhasználásával: abcdefgh1234567890_!
"""

# Program run command in Android:Termux:Python :
runCmd = "python /storage/emulated/0/BitMiller/Pradhana/Dropbox/bitmiller_hu/verebely_progs/programozasi_alapok/gyakorlo_feladatok/feladatok4_pdf/feladat18.py"

from random import randint

chars = "abcdefgh1234567890_"

pwd = ""

for i in range(8):
 pwd += chars[randint(1, len(chars)-1)]

print(f"A jelszó: {pwd}")

"""
s = "abcdabcd"
i = s.index("cd")
print(i)
"""



