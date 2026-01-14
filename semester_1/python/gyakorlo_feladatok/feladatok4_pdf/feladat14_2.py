# @241119-2-1655
# feladat14.pdf

"""
Kérjünk be egy szót és cseréljük le benne a magyar ékezetes betűket az angol ábécé megfelelő ékezet nélküli betűire.
"""

# Program run command in Android:Termux:Python :
runCmd = "python /storage/emulated/0/BitMiller/Pradhana/Dropbox/bitmiller_hu/verebely_progs/programozasi_alapok/gyakorlo_feladatok/feladatok4_pdf/feladat14.py"

ekezetes:str = "áéíóöőúüűÁÉÍÓÖŐÚÜŰ"
ekmentes:str = "aeiooouuuAEIOOOUUU"

s = input("Szöveget: ")
s2 = ""

for c in s:
 if c in ekezetes:

#befejezni ezt a módszert is (Juhász Zolié-szerű)