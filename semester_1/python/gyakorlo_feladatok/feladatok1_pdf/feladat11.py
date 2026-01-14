# @241106-3-2016
# feladat11.py
"""
Zöldséges standunkon háromféle terméket árulunk: almát, szilvát és szőlőt.
A program írja ki a gyümölcs nevét és kilogrammonkénti egységárát, majd kérdezze meg, hogy mennyit szeretnénk vásárolni.
A vásárolt mennyiség mellett jelenjen meg a fizetendő összeg, majd a végösszeget is adjuk meg! (zoldseges)
"""

# Program run command in Android:Termux:Python :
runCmd = "python /storage/emulated/0/BitMiller/Pradhana/Dropbox/bitmiller_hu/verebely_progs/programozasi_alapok/gyakorlo_feladatok/feladatok1_pdf/feladat11.py"

print("Itt a piac. Ezek vannak:\nAlma: 300 Ft/kg\nSzilva: 400 Ft/kg\nSzőlő: 600 Ft/kg\nMiből mönnyi kg köll?")
alma = float(input("Alma: "))*300
szilva = float(input("Szilva: "))*400
szolo = float(input("Szőlő: "))*600

print(f"Itt a számla, Bástya:\nAlma: {alma} Ft\nSzilva: {szilva} Ft\nSzőlő: {szolo} Ft\nVégösszeg: {alma+szilva+szolo} Ft.")

