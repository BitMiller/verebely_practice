# @241119-2-1655
# feladat10.pdf

"""
Kérjünk be egy szót, és cseréljük le az első karakterét nagybetűre!
"""

# Program run command in Android:Termux:Python :
runCmd = "python /storage/emulated/0/BitMiller/Pradhana/Dropbox/bitmiller_hu/verebely_progs/programozasi_alapok/gyakorlo_feladatok/feladatok4_pdf/feladat10.py"

szoveg = input("Acca szó: ")

szoveg2 = szoveg[0].upper()+szoveg[1:]

print(szoveg2)

