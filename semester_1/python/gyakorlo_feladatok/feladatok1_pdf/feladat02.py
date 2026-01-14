# @241105-2-1916
# feladatok1.pdf
"""
2. Olvassunk be két vezeték- és két keresztnevet, és írassuk ki az ezekből képezhető neveket! (nevek)
"""

# Program run command in Android:Termux:Python :
runCmd = "python /storage/emulated/0/BitMiller/Pradhana/Dropbox/bitmiller_hu/verebely_progs/programozasi_alapok/gyakorlo_feladatok/feladatok1_pdf/feladat02.py"


print("Adj be két vezeték-, majd két keresztnevet, szóközökkel elválasztva!")
nevek = input()

nevek = nevek.split(" ")

print("Ezek a nevek lehetségesek belőle:")
print(f"{nevek[0]} {nevek[2]}")
print(f"{nevek[0]} {nevek[3]}")
print(f"{nevek[1]} {nevek[2]}")
print(f"{nevek[1]} {nevek[3]}")
