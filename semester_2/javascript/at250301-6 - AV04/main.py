"""
Feladat kész: 50 perc
@250310-1-1655

Pofásítás, hogy hasonlítson a kért mintához, ennyi idő alatt kész:
60 perc
"""

feladat = 3

if True:
 if True:

#match feladat:
 #case 1:
  print("1. feladat:")
  #valasz = input("J vagy LY van a to_ás szóban?\n(Lehetséges válaszok: j / ly) : ").lower().strip()
  valasz = input("\"j\" vagy \"ly\" van abban a szóban, hogy to_ás?\nválasz: ").lower().strip()
  if valasz == "j":
   print("Hejesiráss: 5öss!")
  elif valasz == "ly":
#   print("Hejesiráss: 1ess!")
   print("sajnos nem, úgy írják, hogy \"tojás\" :(")
  else:
   print("Szövegértelmezés: 1ess!")

############################ 
############################ 
############################ 

 #case 2:
  
  def osztok(szam):
   ig = int(szam**0.5//1)
   oszt:list = []
   for i in range(1, szam+1):
    if szam%i == 0:
     oszt.append(i)
   return oszt
  
  def relativ(szam1, szam2):
   oszt1 = osztok(szam1)
   oszt2 = osztok(szam2)
   #print(f"oszt1: {oszt1}, oszt2: {oszt2}")
   for o in oszt1:
    if o != 1 and o in oszt2:
     return False
   return True
    
  
  print("\n2. feladat:")
  sza1 = int(input("kérem az egyik számot: "))
  sza2 = int(input("kérem a másik számot: "))
  osz1 = osztok(sza1)
  osz2 = osztok(sza2)
  print(f"{sza1} osztói: {osz1}")
  print(f"{sza2} osztói: {osz2}")
  #print(relativ(sza1, sza2))
  if relativ(sza1, sza2):
   print(f"{sza1} és {sza2} relatív prímek!")
  else:
   print(f"{sza1} és {sza2} irrelatív prímek!")
   
  #print(relativ(4,16))
  
 
############################ 
############################ 
############################ 

 #case 3:
  print("\n3. feladat:")
 
  import os
  
  class Versenyzo:
   def __init__(self, ln):
    ln = ln.split(";")
    self.nev = ln[0]
    self.nemzetiseg = ln[1]
    self.csapat = ln[2]
    self.rajt = int(ln[3])
    self.ido = float(ln[4])
    self.pontok = int(ln[5])
    
   def __repr__(self):
    return(f"Versenypilóta:\nNév:\t\t{self.nev}\nNemzetiség:\t{self.nemzetiseg}\nCsapat:\t\t{self.csapat}\nRajt:\t\t{self.rajt}\nIdő:\t\t{self.ido}\nPontok:\t\t{self.pontok}")
  
  os.chdir(os.path.dirname(__file__))
  #print(os.getcwd())
  with open("melbourne2009.txt", "r", encoding="UTF-8") as f:
   data = f.readlines();
  
  versenyzok:list = []
  
  for d in range(1, len(data)):
   versenyzok.append(Versenyzo(data[d]))

  print(versenyzok)

  ossz_pontok:int = 0
  nemet:int = 0
  pontszerzok:list = []
  gyoztes:int = 0
  
  for i in range(len(versenyzok)):
   ossz_pontok += versenyzok[i].pontok
   if versenyzok[i].nemzetiseg == "germany":
    nemet += 1
   if versenyzok[i].pontok != 0 and versenyzok[i].csapat not in pontszerzok:
    pontszerzok.append(versenyzok[i].csapat)
   if versenyzok[i].ido < versenyzok[gyoztes].ido:
    gyoztes = i

  print(f"3.1 feladat: Célba érkező versenyzők száma: {len(versenyzok)}")
  print(f"3.2 feladat: Kiosztott pontok összesen: {ossz_pontok}")
  print(f"3.3 feladat: Német versenyzők száma: {nemet} fő")
  print("3.4 feladat: Pontszerző csapatok:")
  for i in pontszerzok: print(f"\t{i}")
  print(f"3.5 feladat: A verseny győztese: {versenyzok[gyoztes].nev} (1:34:{versenyzok[gyoztes].ido})")
  

