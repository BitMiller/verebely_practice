# @241119-2-1655
# feladat14.pdf

"""
Készítsünk programot, amely -30 °C-tól +30°C-ig kiírja a hőmérsékletet Fahrenheit fok egységekben! (F=1,8*C+32) (homerseklet_atvaltas)
"""

# Program run command in Android:Termux:Python :
runCmd = "python /storage/emulated/0/BitMiller/Pradhana/Dropbox/bitmiller_hu/verebely_progs/programozasi_alapok/gyakorlo_feladatok/feladatok2_pdf/feladat14.py"

for i in range(-30,31) :
 print(f"{i}\u00B0C = {(i*1.8+32):.1f}\u00B0F")
