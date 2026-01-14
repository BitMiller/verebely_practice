# @241119-2-1655
# feladat04.pdf

"""
Kérjünk be egy szót, majd írjuk ki * karakterekkel bekeretezve!
"""

# Program run command in Android:Termux:Python :
runCmd = "python /storage/emulated/0/BitMiller/Pradhana/Dropbox/bitmiller_hu/verebely_progs/programozasi_alapok/gyakorlo_feladatok/feladatok4_pdf/feladat04.py"

inp = input("Adj egy szót!")

for _ in range(len(inp)+2):
 print("*", end="")

print(f"\n*{inp}*\n")

for _ in range(len(inp)+2):
 print("*", end="")

