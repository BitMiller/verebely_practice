# @241106-3-2016
# feladat12.py
"""
Programunk kérje be egy hordó és egy kancsó térfogatát literekben mérve egész számként!
Szeretnénk tudni, hogy hány teli kancsó mérhető ki a hordóból, mennyi víz marad a hordóban a teli kancsók kimerése után.
Mennyi a hordó és a kancsó térfogatának hányadosa? (hordo)
"""

# Program run command in Android:Termux:Python :
runCmd = "python /storage/emulated/0/BitMiller/Pradhana/Dropbox/bitmiller_hu/verebely_progs/programozasi_alapok/gyakorlo_feladatok/feladatok1_pdf/feladat12.py"


# > https://www.geeksforgeeks.org/convert-string-to-integer-in-python/

def require_int_input(s = ""):
 if s!="":
  print(s)

 while True:
  in1 = input()
  try:
   in2 = int(in1)
  except ValueError:
   print("Énnekem egész számot aggyá! : ", end="")
  else: break;

 return in2

hordo = require_int_input("Mekkoraja hordó?")
kancso = require_int_input("Oszt a kancsó?")



"""
hordo = round(float(input("Hordó? : ")))
kancso = round(float(input("Kancsó? : ")))
"""

print("Ennyi kancsónyi víz a hordóban: "+f"{int(hordo/kancso):.2f}")
print(f"És ennyi litteer marad: {hordo%kancso}")
