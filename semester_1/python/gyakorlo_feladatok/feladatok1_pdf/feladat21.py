# @241106-3-2016
# feladat21.py
"""
Két beolvasott számot írassunk ki úgy, hogy közéjük tesszük a megfelelő relációs jelet (<,>,=)! (relacio)
"""

# Program run command in Android:Termux:Python :
runCmd = "python /storage/emulated/0/BitMiller/Pradhana/Dropbox/bitmiller_hu/verebely_progs/programozasi_alapok/gyakorlo_feladatok/feladatok1_pdf/feladat21.py"


def gyere_szam_be(s=""):
 if s!="": print(s+" : ", end="")
 repeat = True;
 while repeat:
  inp = input()
  try: res = float(inp)
  except ValueError:
   print("Na, most menj el szépen, gondold át az életedet, gyere vissza, és adj meg egy normális inputot!", end=" : ")
  else: repeat = False
 return res


szam1 = gyere_szam_be("Alázatossan naccsos úr, adjon nekem valami számot!")
szam2 = gyere_szam_be("Tudja, mi a stájsz, ha a kisujját nyújtja...")

szam1_str = str(round(szam1, 2)).rstrip("0").rstrip(".")
szam2_str = str(round(szam2, 2)).rstrip("0").rstrip(".")

print(f"{szam1_str} {'<' if szam1<szam2 else '>' if szam1>szam2 else "="} {szam2_str}")

#print(f"Igazából {szam1} {szam2}")

