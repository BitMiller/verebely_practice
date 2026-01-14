# @241119-2-1655
# feladat01.pdf

"""
Hozzunk létre egy 5 elemű tömböt, amiben helyezzünk el 5 nevet!
a. Írassuk ki a neveket a képernyőre!
b. Hozzunk létre egy 5 elemű, egész típusú tömböt, amelyben az 5 ember magasságát fogjuk tárolni, és kérjük be a magasságokat billentyűzetről!
c. Számoljuk ki az 5 ember átlagmagasságát!
d. Rendezzük a neveket tartalmazó tömböt névsorba!
e. Ki a legmagasabb és hány cm? Rendezzük magasság szerint növekvő sorba őket!
"""

# Program run command in Android:Termux:Python :
runCmd = "python /storage/emulated/0/BitMiller/Pradhana/Dropbox/bitmiller_hu/verebely_progs/programozasi_alapok/gyakorlo_feladatok/feladatok3_pdf/feladat01.py"

nevek = ["Mari", "Feri", "Teri", "Juli", "Matyi"]

for i in nevek:
 print(i)

magassagok:list[int] = []

for i in range(len(nevek)) :
 magassagok.append(int(input(f"{nevek[i]} magassága: ")))

print(magassagok)

szum_magassagok = 0
for i in range(len(nevek)) :
 szum_magassagok += magassagok[i]

atlag_magassag = szum_magassagok/len(magassagok)

print(f"Átlag magasság: {atlag_magassag:.2f}")


print("Emberkék magasságai ábécés rendezés előtt:")
for i in range(len(nevek)) :
 print("befejezni")

for i in range(len(nevek)-1) :
 for j in range(i+1, len(nevek)) :
  if nevek[i]>nevek[j] :
   tmp = nevek[i]
   nevek[i] = nevek[j]
   nevek[j] = tmp
   tmp = magassagok[i]
   magassagok[i] = magassagok[j]
   magassagok[j] = tmp

print()
