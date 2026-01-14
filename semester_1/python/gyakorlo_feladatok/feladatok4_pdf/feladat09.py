# @241119-2-1655
# feladat09.pdf

"""
Írassunk ki egy szöveget csupa nagybetűvel/ kisbetűvel.
"""

# Program run command in Android:Termux:Python :
runCmd = "python /storage/emulated/0/BitMiller/Pradhana/Dropbox/bitmiller_hu/verebely_progs/programozasi_alapok/gyakorlo_feladatok/feladatok4_pdf/feladat09.py"

inp = input("Acca szöveg: ")

print(f"Csupi kics bötü: {inp.lower()}")
print(f"Csupi nagy bötü: {inp.upper()}")
print(f"Csupi nagy kezdöbötüs kis bötü: {inp.title()}")

