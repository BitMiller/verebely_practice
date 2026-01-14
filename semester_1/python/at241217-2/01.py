
sorozat:list[int] = [26, 2, 11, 7, 42, 7, 34]

# SOROZATSZÁMÍTÁS TÉTELÉnek megvalósítása az összegzésre (kissé helytelenül: összegzés tétele) :
# sorozat elemei összegének meghatározása
sum:int = 0 # a műveletre neutrális érték a kezdőérték, szorzásnál ez 1 lenne; string konkatenációnál: ""
for szam in sorozat:
 sum += szam
#print(sum)

# MEGSZÁMLÁLÁS:
# megadja a <T> tulajdonságú elemek számát a sorozatban
# a kezdeti változó típusa azonos a sorozat elemeinek típusával; illetve a számláló változó értéke mindig egész, kezdőértéke mindig 0
# itt a páros elemek számát akarom meghatározni
darab:int = 0
for szam in sorozat:
 if szam % 2 == 0:
  darab += 1
#print(darab)

# SZÉLSŐÉRTÉK MEGHATÁROZÁS:

mini:int = 0 # nem-negatív egész számok esetén, tehát ez az algoritmus nem általános
for index in range(1, len(sorozat)):
 if sorozat[index] < sorozat[mini]:
  mini = index
#print(str(mini) + ":" + str(sorozat[mini]) + f" Ez a sorozat {mini+1}-ik eleme.")

maxi:int = 0
for index in range(1, len(sorozat)):
 if sorozat[index] > sorozat[maxi]:
  maxi = index
#print(str(maxi) + ":" + str(sorozat[maxi]) + f" Ez a sorozat {maxi+1}-ik eleme.")

# LINEÁRIS KERESÉS:
keresett:int = 5

index:int = 0
while index < len(sorozat) and sorozat[index] != keresett:
 index += 1
if index < len(sorozat):
 print(f"Van találat: {index}:{}")

 # KIVÁLASZTÁS:
 # csak akkor alkalmazható, ha az inputot biztosan tartalmazza a sorozat

 irany:str = "balra"


 # ELDÖNTÉS:
 # pl.: van-e a sorozatban 3-val osztható szám?

 # KIVÁLOGATÁS:
 paratlanok:list[int] = []

 for szam in sorozat:
  if szam % 2 == 1:
   paratlanok.append(szam)

# ... stb, Juhász Zoli GitHub-járól leszedni a fájlt, megnézni, mit írt bele!
 




