# @241106-3-2016
# feladat17.py
"""
Kérdezzük meg a felhasználótól, hogy szeret-e programozni, ha igen, akkor írassunk ki,
hogy „Még sokra viszed az életben!”, majd köszönjön el a program (Viszontlátásra!). (kerdes)
"""

# Program run command in Android:Termux:Python :
runCmd = "python /storage/emulated/0/BitMiller/Pradhana/Dropbox/bitmiller_hu/verebely_progs/programozasi_alapok/gyakorlo_feladatok/feladatok1_pdf/feladat17.py"

valaszok = [
["","1","y","i","igen","persze","hogyne","miazhogy","naná",],
["0","n","nem","isten őrizzen","dehogy","dehogyis",]
]

def valasz_be(s=""):
 if s!="": print(s+" : ", end="")
 global valaszok
 valasz = None
 while valasz == None:
  s_in = input().lower()
  if s_in in valaszok[0]: valasz = True
  elif s_in in valaszok[1]: valasz = False
  else: print("Aggyámá nómális válaszot! (1=igen, 0=nem, vagy valami) : ", end="")
 return valasz;

nev = input("Hogy hívják a nevedet? : ")
szeret_e = valasz_be(f"Szeret-e programozni, {nev}?")

#print(f"Megtudtuk, {nev}{szeret_e ? '' : ' nem'} szeret programozni.")
print(f"Megtudtuk, {nev}{'' if szeret_e else ' nem'} szeret programozni.")
if szeret_e: print(f"Kedves {nev}, még sokra viszed az életben!")
print("Nah, viszlát!")

