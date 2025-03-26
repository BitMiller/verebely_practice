
"""

Feladatok hibátlanok ennyin belül: 1ó 15p


Az output tökéetes formátumú a 3. feladathoz, amihez példa volt,
és az összes feladat eredményét egyhúzásra kiírja ennyin belül: 1ó 25p


"""

from random import *

feladat = 3

if True:
 if True:
#match feladat:
 #case 1:
  print("Feladat 1:")
  
  szamok:list = []
  betuk:list = ["A", "B", "C", "D", "E", "F"]
  
  for i in range(6):
   szamok.append(randint(2, 5))
   for j in range(szamok[i]):
    print(betuk[i], end="")
   print(" ", end="")

####################
####################
####################

 #case 2:
  print("\n\nFeladat 2:")
  
  def strip_acc(s):
   acc_1 = ["á", "é", "í", "ó", "ö", "ő", "ú", "ü", "ű"]
   acc_2 = ["a", "e", "i", "o", "o", "o", "u", "u", "u"]
   rs: str = ""
   for c in s:
    if c in acc_1:
     rs += acc_2[acc_1.index(c)]
    else:
     rs += c
   return rs
     
  def strip_nonalpha(s):
   rs = ""
   exc = [" ","?","!",".",":",";",",",]
   for c in s:
    if c not in exc:
     rs += c
   return rs
  
  #szoveg:str = input("Írj be valami mondatot, kérlek! : ")
  szoveg = "Ez egy tesztmondat, árvíztűrő tükörfúrógép! ÁÉÍÓÖŐÚÜŰ."
  s = szoveg.lower()
  s = strip_acc(s)
  s = s.title()
  s = strip_nonalpha(s)
  print(s)




####################
####################
####################

 #case 3:
  print("\nFeladat 3:")

  import os
  
  class Hallgato:
   def __init__(self, s):
    d = s.split(";")
    self.nev = d[0]
    self.nem = d[1]
    self.befizetes = int(d[2])
    self.targyak = [int(d[3]), int(d[4]), int(d[5]), int(d[6])]
    self.osszpont = int(d[3]) + int(d[4]) + int(d[5]) + int(d[6])
    
   def __str__(self):
    return(f"Hallgató neve: {self.nev}, neme: {self.nem}, eddigi befizetése: {self.befizetes}, félévi vizsgaeredményei:\n\thálózat: {self.targyak[0]}\n\tmobil: {self.targyak[1]}\n\tfrontend: {self.targyak[2]}\n\tbackend: {self.targyak[3]}")
  
  targyak = ["hálózat","mobil","frontend","backend"]
  
  os.chdir(os.path.dirname(__file__))
  #print(os.getcwd())
  
  with open("course.txt", "r", encoding="UTF-8") as f:
   data = f.readlines()
   
  hallgatok:list = []
  
  for i in data:
   hallgatok.append(Hallgato(i))
   #print(hallgatok[len(hallgatok)-1])
   
  #print(f"{}")
  #print(f"Ennyi hallgató van a fájlban: {len(hallgatok)}")
  print(f"3.1: hallgatók száma: {len(hallgatok)} fő")
  
  atlag:int = 0
  for i in range(len(hallgatok)):
   atlag += hallgatok[i].targyak[3]
  atlag /= len(hallgatok)
  #print(f"Ennyi az átlag backend-ből: {atlag}")
  print(f"3.2: hallgatók tanulmányi átlaga backend-ből: {atlag}%")
  
  elso_idx:int = 0
  for i in range(len(hallgatok)):
   if hallgatok[i].osszpont > hallgatok[elso_idx].osszpont:
    elso_idx = i
    
  #print(f"Osztályelső: {hallgatok[elso_idx].nev}")   
  print(f"3.3: legjobb átlagú hallgató neve: {hallgatok[elso_idx].nev}")   

  #print("Ők fizettek be mindent:")
  print("3.4: a következő hallgatók már kifizették a tanfolyam árát:")
  teljes:list = []
  for i in range(len(hallgatok)):
   if hallgatok[i].befizetes == 2600:
    #if len(teljes) != 0: print(", ", end="")
    #print(hallgatok[i].nev, end="")
    print(f"\t\t- {hallgatok[i].nev}")
    teljes.append(i)
    
  print()
  
  #hall:str = input("Kérem egy tanuló nevét! : ").lower()
  hall:str = input("3.5: Írja be a keresett hallgató nevét: ").lower()
  idx:int = -1
  for i in range(len(hallgatok)):
   if hallgatok[i].nev.lower() == hall:
    idx = i
    break
   
  if idx == -1:
   print("Nincs ilyen tanuló!")
   
  else:
   jav:bool = False
   tan:list = []
   for i in range(4):
    if hallgatok[idx].targyak[i] < 51:
     tan.append(i)
      
   if len(tan) == 0:
    print("Zseniális, nem kell javítóvizsgát tennie!")
   else:
    #print("C-c-c, hát bizony javítóvizsgát kell tennie ebből:")
    print(f"\t{hallgatok[idx].nev}-nak/nek az alábbi modulokból kell javítóvizsgát tennie:")
    for i in range(len(tan)):
     #print(targyak[tan[i]])
     print(f"\t\t- {targyak[tan[i]]} ({hallgatok[idx].targyak[tan[i]]}%-os eredmény)")
    

  #print(data)
  


