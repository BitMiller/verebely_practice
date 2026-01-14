# @241119-2-1655
# feladat08.pdf

"""
Döntsd el a beírt mondat típusát! (kijelentő/kérdő/felszólító)
"""

# Program run command in Android:Termux:Python :
runCmd = "python /storage/emulated/0/BitMiller/Pradhana/Dropbox/bitmiller_hu/verebely_progs/programozasi_alapok/gyakorlo_feladatok/feladatok4_pdf/feladat08.py"

inp = input("Mondatot írjá'! : ")

match inp[-1]:
 case "!": print("felordító")
 case "?": print("kérdő")
 case ".": print("kijelentő")
 case _: print("semmilyen.")

