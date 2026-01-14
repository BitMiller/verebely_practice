# @241116-6-1534
# feladat08.py
"""
Programunk kérje be egy autó fogyasztását (literben 100 km-en), a benzin literenkénti árát és a megteendő 

út hosszát, majd számítsa ki az útiköltséget! (uzemanyag)
"""

# Program run command in Android:Termux:Python :
runCmd = "python /storage/emulated/0/BitMiller/Pradhana/Dropbox/bitmiller_hu/verebely_progs/programozasi_alapok/gyakorlo_feladatok/feladatok1_pdf/feladat09.py"


fogyi = float(input("Mennyit eszik a ótód? (L/100km) : "))
benya = float(input("Osz' hogyé' a litya? (Ft/L) : "))
menyen = float(input("Osz mennyit menyel? (km) : "))

print("Ennyibe fáj: "+str(fogyi/100*menyen*benya)+" Ft")

