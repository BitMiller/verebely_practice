# @241106-3-2016
# feladat23.py
"""
Írjunk programot, amely értékel egy dolgozatot a rá adott pontszám alapján! Az értékelés a következő táblázat alapján történjen:
Pontszám Értékelés
0 - 42 elégtelen
43 - 57 elégséges
58 - 72 közepes
73 - 87 jó
88 - 100 jeles
"""

# Program run command in Android:Termux:Python :
runCmd = "python /storage/emulated/0/BitMiller/Pradhana/Dropbox/bitmiller_hu/verebely_progs/programozasi_alapok/gyakorlo_feladatok/feladatok1_pdf/feladat23.py"


intervals = [
{"jegy" : "elégtelen", "tól" : 0, "ig" : 42},
{"jegy" : "elégséges", "tól" : 43, "ig" : 57},
{"jegy" : "közepes", "tól" : 58, "ig" : 72},
{"jegy" : "jó", "tól" : 73, "ig" : 87},
{"jegy" : "jeles", "tól" : 88, "ig" : 100},
]

jegy = int(input("Hány a pontszám? (0-100-ig, egész számot!) : "))


#print(intervals[1]["jegy"])


for i in intervals:
 if jegy>=i["tól"] and jegy<=i["ig"]:
  print(f"Ez a doga biza {i['jegy']}!!!")
  break


