# @241119-2-1655
# feladat03.pdf

"""
Számoljon vissza a program 10-től egyesével (mondjuk másodpercenként), majd írja ki, hogy lejárt az időd és kis idő múlva lépjen ki! (visszaszamol)
"""

# Program run command in Android:Termux:Python :
runCmd = "python /storage/emulated/0/BitMiller/Pradhana/Dropbox/bitmiller_hu/verebely_progs/programozasi_alapok/gyakorlo_feladatok/feladatok2_pdf/feladat03.py"

import time
import os


print("Visszaszámlálás indul!")
for i in range(10,0,-1):
 time.sleep(0.2)
 print(i)

time.sleep(0.2)
print("Lejárt az időd!")
time.sleep(2)
os.system("cls")
time.sleep(2)
