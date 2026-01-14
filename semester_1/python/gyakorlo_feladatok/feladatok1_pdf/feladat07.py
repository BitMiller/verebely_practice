# @241105-2-1956
# feladat07.py
"""
7. Írjunk programot a Pitagorasz-tétel alkalmazására! A program kérje be egy derékszögű háromszög két 
befogóját, és számítsa ki az átfogó hosszát! (pitagorasz)
"""

# Program run command in Android:Termux:Python :
runCmd = "python /storage/emulated/0/BitMiller/Pradhana/Dropbox/bitmiller_hu/verebely_progs/programozasi_alapok/gyakorlo_feladatok/feladatok1_pdf/feladat07.py"

from math import sqrt

bef_1 = int(input("Egyik befogó: "))
bef_2 = int(input("Másik befogó: "))
print(f"Így elmondhatjuk, hogy átfogó ismeretekkel rendelkezünk a háromszögről: {sqrt(bef_1**2+bef_2**2)}")



