# @241106-3-2016
# feladat22.py
"""
Egy beolvasott számról döntse el a program hogy -30 és 40 között van-e! (kozotte)
"""

# Program run command in Android:Termux:Python :
runCmd = "python /storage/emulated/0/BitMiller/Pradhana/Dropbox/bitmiller_hu/verebely_progs/programozasi_alapok/gyakorlo_feladatok/feladatok1_pdf/feladat22.py"


def szam_be(s=""):
 if s!="": print(s, end=" : ")
 repeat = True
 while repeat:
  inp = input()
  try: res = float(inp)
  except ValueError: print("No, még1x, csak máshogy!", end=" : ")
  else: repeat = False
 return res


#szam = 0

szam = szam_be("Jöhet egy szám (akár negatív)!")

kozott_e = True if szam>-30 and szam<40 else False

print(f"Ez a szám mostan jelenleg {'' if kozott_e else 'nincs '}-30 és 40 között{' van' if kozott_e else ''}.")

#print(4 if False else 3)

