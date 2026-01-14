# @241105-2-1931
# feladat06.py
"""
6. Írjunk programot, amely bekéri egy kör sugarát, és kiszámolja a kör kerületét és területét! (kor_ker_ter)
"""

# Program run command in Android:Termux:Python :
runCmd = "python /storage/emulated/0/BitMiller/Pradhana/Dropbox/bitmiller_hu/verebely_progs/programozasi_alapok/gyakorlo_feladatok/feladatok1_pdf/feladat06.py"


from math import *

teljes_ertek = 0

radius = float(input("Adgyad már meg a kör sugarát! : "))
print(f"E itt a kerület: {(teljes_ertek:=radius*2*pi):.3f} egység")
print(f"E itt a terület: {round(radius**2*pi, 3)} egység^2")

print(teljes_ertek)