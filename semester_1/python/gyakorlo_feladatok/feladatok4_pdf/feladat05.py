# @241119-2-1655
# feladat05.pdf

"""
Kérjünk be egy tetszőleges szöveget, és írassuk ki fordítva!
"""

# Program run command in Android:Termux:Python :
runCmd = "python /storage/emulated/0/BitMiller/Pradhana/Dropbox/bitmiller_hu/verebely_progs/programozasi_alapok/gyakorlo_feladatok/feladatok4_pdf/feladat05.py"

inp = input("Hoci szöveg: ")

#print(str(reversed(inp)))

#print(inp[::-1])

#for i in range(len(inp), 0, -1):
# print(inp[i-1], end="")

#for i in range(len(inp)):
# print(inp[len(inp)-i-1], end="")

for i in range(len(inp)):
 print(inp[-i-1], end="")

