
"""
Feladat kész: @250313-4-1657 33p
"""


import os

os.chdir(os.path.dirname(__file__))

class Kategoria:
 def __init__(self, s):
  s = s.strip().split(";")
  self.nev = s[0]
  self.tulelo = int(s[1])
  self.eltunt = int(s[2])
  self.ossz = self.tulelo+self.eltunt
  
 def __repr__(self):
  return(f"\nKategória: {self.nev} | Túlélő: {self.tulelo} | Eltűnt: {self.eltunt}")

with open("titanic.txt", "r", encoding="UTF-8") as f:
 data = f.readlines()
 
kategoriak:list = []

for d in data:
 kategoriak.append(Kategoria(d))
 
#print(sorok)

ossz_letszam:int = 0

for i in range(len(kategoriak)):
 ossz_letszam += kategoriak[i].tulelo + kategoriak[i].eltunt

#print(f"{}")

print(f"2. feladat: {len(kategoriak)} db")
print(f"3. feladat: {ossz_letszam} fő")

keres:str = input("4. feladat: Kulcsszó: ")
keres_idxs:list = []
eltuntek_60_idxs:list = []
legtobb_tulelo_idx:int = 0
for i in range(len(kategoriak)):
 if keres.lower() in kategoriak[i].nev.lower():
  keres_idxs.append(i)
 if kategoriak[i].eltunt/kategoriak[i].ossz > 0.6:
  eltuntek_60_idxs.append(i)
 if kategoriak[i].tulelo > kategoriak[legtobb_tulelo_idx].tulelo:
  legtobb_tulelo_idx = i

if keres_idxs == []:
 print("\tNincs találat!")
else:
 print("\tVan találat!\n5. feladat:")
 for k in keres_idxs:
  print(f"\t{kategoriak[k].nev} {kategoriak[k].tulelo + kategoriak[k].eltunt} fő")
 
print("6. feladat:")
for e in eltuntek_60_idxs:
 print(f"\t{kategoriak[e].nev}")
 
print(f"7. feladat: {kategoriak[legtobb_tulelo_idx].nev}")