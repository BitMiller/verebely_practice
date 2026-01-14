# @241105-2-1923
# feladat04.py
"""
4. Programunk kérje be az Euró árfolyamát (1 € hány Ft-ot ér), majd azt, hogy hány eurót akarunk átváltani 
Ft-ba, majd írja ki, hogy hány Ft az átváltott euró. (euro)
"""

# Program run command in Android:Termux:Python :
runCmd = "python /storage/emulated/0/BitMiller/Pradhana/Dropbox/bitmiller_hu/verebely_progs/programozasi_alapok/gyakorlo_feladatok/feladatok1_pdf/feladat04.py"


arfolyam = float(input("Hoci a euró árfolyama: "))
forint = int(input("Oszt mennyi a váltandó della? : "))
print(f"Hát ez így bizony {forint*arfolyam:,} arany pengő Euro lesz!")

