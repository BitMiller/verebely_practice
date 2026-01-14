# @241119-2-1655
# feladat07.pdf

"""
Szimuláljunk egy lottóhúzást!
a. A kihúzott számokat növekvő sorrendben írjuk ki!
b. A lottóhúzás előtt adjuk meg a tippjeinket (ügyelve rá, hogy 5 különböző számot kelljen megadni) és a húzás után írjuk ki, hogy hány találatunk volt!
"""

"""
Megjegyzésem #p
Az a nagy baj ezzel a lottós feladattal, hogy ha sikerül valakinek eltalálni a saját programja által generált számokat, akkor több ezer évre elveszítheti a lottónyerési esélyét.

Bár, ha leszkrínsotolja, és beküldi a forráskóddal együtt a Szer Zrt-nek, lehet, fizetnek valamennyit... Legalábbis megvan az esélye :D

Ellenben, ha nem nyer, pedig egy for ciklussal lefuttatta egymilliószor, akkor pont hogy megnövelte az esélyeit...

Erre mondja a vicc, jobb a férfiaknak, mert nekik minden húzásnál milliók ütik a markukat...
"""


# Program run command in Android:Termux:Python :
runCmd = "python /storage/emulated/0/BitMiller/Pradhana/Dropbox/bitmiller_hu/verebely_progs/programozasi_alapok/gyakorlo_feladatok/feladatok3_pdf/feladat07.py"


from random import randint

def get_int_input(s = ""):
 if s!="":
  print(s)
 while True:
  inp1 = input()
  try:
   inp2 = int(inp1)
  except ValueError:
   print("Int-et adgyá! : ", end="")
  else: return(inp2)


max_szam = {
 "5" : 90,
 "6" : 45,
 "7" : 35
}

tippek = []


print("Most jön a lottóhúzás! Add meg, milyen lottót akarsz játszani (5, 6 v. 7 (skandi)) : ")

while True:
 jatekfajta = input()
 if jatekfajta!="5" and jatekfajta!="6" and jatekfajta!="7":
  print("Aggyámá nórmális választ!")
 else: break

szamok_szama = int(jatekfajta)

print(f"Ezt választottad: {jatekfajta}-ös/-os/-es lottó")
print(f"1-től {max_szam[jatekfajta]}-ig tippelhetsz!")

print(f"Na, hát akkor lássuk a számaidat! Tippelj egyenként {szamok_szama}db-ot!")

for i in range(szamok_szama):
 print(f"{i+1}. tipped: ")
 while True:
  tipp = get_int_input()
  if tipp not in tippek:
   tippek.append(tipp)
   break
  else: print("Ilyen számod van már, he! Na még1x! : ")

tippek.sort()

huzasok = []

for i in range(szamok_szama):
 #print(tippek[i])
 while True:
  huzas = randint(1, max_szam[jatekfajta])
  if huzas not in huzasok:
   huzasok.append(huzas)
   break

huzasok.sort()

talalatok = 0

for i in range(szamok_szama):
 if tippek[i] == huzasok[i]:
  talalatok+=1

print(f"Tippjeid: {tippek}")
print(f"Húzások : {huzasok}")
print(f"Találataid száma: {talalatok}")
print("Szevasz!")


