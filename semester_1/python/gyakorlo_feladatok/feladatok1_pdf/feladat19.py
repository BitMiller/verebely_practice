# @241106-3-2016
# feladat19.py
"""
Olvassunk be egy számot a billentyűzetről, és írjuk ki, hogy osztható-e 3-mal! (oszthato3)
"""

# Program run command in Android:Termux:Python :
runCmd = "python /storage/emulated/0/BitMiller/Pradhana/Dropbox/bitmiller_hu/verebely_progs/programozasi_alapok/gyakorlo_feladatok/feladatok1_pdf/feladat19.py"


def beker(s=""):
 if s!="": print(s+" : ", end="")
 while True:
  inp = input()
  try: res = float(inp)
  except ValueError: print("Nem lesz jó. No, még egyszer! : ")
  else:
   try: res = int(inp)
   except ValueError: print("Az oké, hogy szám, de ha a tizedestört rész nem nulla, tuti, hogy nem osztható 3-val! : ")
   else: return res


szam = beker("Olvastass be egy számot a billentyűzetről! : ")

print(f"A szám {'nem ' if szam%3!=0 else ""}osztható 3-val.")
