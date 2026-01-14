"""
Végeztem: @250314-5-1723 1ó4p
"""

import os

class Barlang:
 def __init__(self, ln):
  ln = ln.strip().split(";")
  
  self.azon = int(ln[0])
  self.nev = ln[1]
  self.hossz = int(ln[2])
  self.melyseg = int(ln[3])
  self.telepules = ln[4]
  self.vedettseg = ln[5]
  
 def __repr__(self):
  return(f"Azonosító: {self.azon}\nNév: {self.nev}\nHossz: {self.hossz}m\nMélység: {self.melyseg}\nTelepülés: {self.telepules}\nVédettség: {self.vedettseg}\n")

os.chdir(os.path.dirname(__file__))

with open("barlangok.txt", "r", encoding="UTF-8") as f:
 data = f.readlines()
 
barlangok:list = []

for i in range(1, len(data)):
 barlangok.append(Barlang(data[i]))

#print(barlangok)
#print(barlangok[len(barlangok)-1])

miskolci_idxs:list = []

for i in range(len(barlangok)):
 if barlangok[i].telepules.lower().startswith("miskolc"):
  miskolci_idxs.append(i)
  print(barlangok[i].nev)

miskolci_atlag:int = 0
for i in range(len(miskolci_idxs)):
 miskolci_atlag += barlangok[miskolci_idxs[i]].melyseg
if miskolci_idxs == []:
 formazott = 0
else:
 miskolci_atlag /= len(miskolci_idxs)
 formazott = str(f"{miskolci_atlag:.3f}").replace(".",",")
 
print(f"4. feladat: Barlangok száma: {len(barlangok)}")
print(f"5. feladat: Az átlagos mélység: {formazott} m")
vedettsegi_szint = input("6. feladat: Kérem a védettségi szintet: ")
 
leghosszabb_vedett_idx:int = -1
for i in range(len(barlangok)):
 if barlangok[i].vedettseg.lower() == vedettsegi_szint.lower() and (leghosszabb_vedett_idx == -1 or barlangok[i].hossz > barlangok[leghosszabb_vedett_idx].hossz):
   leghosszabb_vedett_idx = i

if leghosszabb_vedett_idx == -1:
 print("\tNincs ilyen védettségi szinttel barlang az adatok között!")
else:
 print(f"\tAzon: {barlangok[leghosszabb_vedett_idx].azon}")
 print(f"\tNév: {barlangok[leghosszabb_vedett_idx].nev}")
 print(f"\tHossz: {barlangok[leghosszabb_vedett_idx].hossz}")
 print(f"\tMélység: {barlangok[leghosszabb_vedett_idx].melyseg}")
 print(f"\tTelepülés: {barlangok[leghosszabb_vedett_idx].telepules}")
 
vedett_fajta:list = [str]
vedett_mennyiseg:dict = {}

for i in range(len(barlangok)):
 if vedett_fajta == [] or barlangok[i].vedettseg not in vedett_fajta:
  vedett_fajta.append(barlangok[i].vedettseg)
  vedett_mennyiseg.update({barlangok[i].vedettseg : 1})
 else:
  vedett_mennyiseg[barlangok[i].vedettseg] += 1
  
#print(vedett_mennyiseg)

print("7. feladat: Statisztika")

#vedett_formazott:dict = {}
for k, v in vedett_mennyiseg.items():
 s = "\t" + k + ":"
 for i in range(28-len(k)):
  s += "-"
 print(f"{s}> {v} db")


