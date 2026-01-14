# @241106-3-2016
# feladat18.py
"""
Kérjünk be egy egész számot, és írassuk ki hogy az adott szám páros-e vagy sem. (paritas)
"""

# Program run command in Android:Termux:Python :
runCmd = "python /storage/emulated/0/BitMiller/Pradhana/Dropbox/bitmiller_hu/verebely_progs/programozasi_alapok/gyakorlo_feladatok/feladatok1_pdf/feladat18.py"


def beker(s=""):
 if s!="":
  print(s+" : ", end="")
 while True:
  inp = input()
  try:
   inp = int(inp)
  except ValueError:
   print("No, akkor most még egyszer, mert ez nem az! : ", end="")
  else: return inp



szam = beker("Kérlek szépen, adj meg egy egész számot!")

print(f"A szám pár{'os' if szam%2==0 else 'atlan'}.")


