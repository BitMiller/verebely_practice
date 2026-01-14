
"""

Végeztem:
1ó 25p alatt @250301-6-1241

"""

feladat = 3

###################################
###################################
###################################

match feladat:
 case 1:
  print("1. feladat:")
  szul = int(input("Születési éved? : "))
  print(f"Ennyi leszel/vagy 2023-ban: {2023-szul}")

###################################
###################################
###################################

 case 2:
  print("2. feladat:")

  SOFOR_ORADIJ = 3950
  UTAK_KM_ARA = 165
  ATLAGFOGYASZTAS = 6.3/100
  DIZEL_LITER_ARA = 566.6 #633.3

  class Ut:
   def __init__(self, nev, tav, perc):
    self.nev = nev
    self.tav = tav
    self.perc = perc
    self.ora = perc/60

   def __str__(self):
    return(f"Név: {self.nev}, táv: {self.tav}km, Idő percben: {self.perc}p, Idő órában: {self.ora}ó")
   
  def keres(ut_str):
   global utak
   for i in range(len(utak)):
    if utak[i].nev == ut_str:
     return i
   return -1

  utak = [
   Ut("bm", 187, 119),
   Ut("mb", 185, 120),
   Ut("bd", 233, 140),
   Ut("db", 233, 146),
   Ut("md", 115, 75),
   Ut("dm", 115, 78),
  ]



  print("Honnan hová akarsz utazni? Lehetséges válaszok:")
  print("Budapest = b, Miskolc = m, Debrecen = d")
  varos1 = input("Honnan? : ").lower()
  varos2 = input("Hová? : ").lower()
  utasok_szama = int(input("Hányan utaztok? : "))
  kocsik_szama = (utasok_szama-1)//8+1 # Gondolkodásom: ha egy kocsi 9 személyes, azt jelenti, hogy 8 utas + 1 sofőr: minden megkezdett 8 utasra kell 1 sofőr!
  #print(f"{kocsik_szama} db. kocsira lesz szükség.")

  ut_str = varos1+varos2
  ut_index = keres(ut_str)
  #print(f"Út tulajdonságai: {utak[ut_index]}")
  #print(f"UTAK_KM_ARA*utak[ut_index].tav: {UTAK_KM_ARA*utak[ut_index].tav}")
  #print(f"SOFOR_ORADIJ*utak[ut_index].ora: {SOFOR_ORADIJ*utak[ut_index].ora}")
  #print(f": {}")

  sofor_koltseg_1fo = SOFOR_ORADIJ*utak[ut_index].ora
  sofor_koltseg_ossz = sofor_koltseg_1fo*kocsik_szama
  #print(f"sofor_koltseg_1fo: {sofor_koltseg_1fo}")
  #print(f"sofor_koltseg_ossz: {sofor_koltseg_ossz}")

  koltseg_ossz = (UTAK_KM_ARA*utak[ut_index].tav+SOFOR_ORADIJ*utak[ut_index].ora)*kocsik_szama
  koltseg_1szemely = koltseg_ossz/utasok_szama

  print(f"Összes költség {kocsik_szama} kocsira: {koltseg_ossz} Ft")
  print(f"Költség 1 személyre: {koltseg_1szemely} Ft")

  uzemanyag_1kocsi = DIZEL_LITER_ARA*ATLAGFOGYASZTAS*utak[ut_index].tav
  uzemanyag_ossz = uzemanyag_1kocsi*kocsik_szama
  #print(f"uzemanyag_1kocsi: {uzemanyag_1kocsi}")
  #print(f"uzemanyag_ossz: {uzemanyag_ossz}")

  bevetel = koltseg_ossz-sofor_koltseg_ossz-uzemanyag_ossz

  print(f"A furaros cég bevétele: {bevetel} Ft")

###################################
###################################
###################################

 case 3:
  print("3. feladat:")

  import os
  os.chdir(os.path.dirname(__file__))
  #print(os.getcwd())

  class Termek:
   def __init__(self, s):
    s = s.strip().split(";")
    self.nev = s[0]
    self.ar = int(s[1])
    self.db = int(s[2])

   def __str__(self):
    return(f"Termék neve: {self.nev}, ára: {self.ar} Ft, készlete: {self.db} db")
   
  def keres(nev):
   global termekek
   for i in range(len(termekek)):
    #print(f"nev : termekek[i].nev: {nev} : {termekek[i].nev} : {nev == termekek[i].nev}")
    if nev == termekek[i].nev.lower():
     return i
   return -1
  
  with open("vm2023.txt", "r", encoding="UTF-8") as f:
   data = f.readlines()

  termekek:list = []

  for i in range(len(data)):
   termekek.append(Termek(data[i]))

  print("Az automatában lévő termékek:")
  for i in termekek: print(i)

  print(f"Az automatában {len(termekek)} db termék van.")

  osszertek:int = 0
  ossz_200ft:int = 0
  legdragabb_index:int = 0

  for i in range(len(termekek)):
   osszertek += termekek[i].ar*termekek[i].db
   if termekek[i].ar <= 200:
    ossz_200ft += 1
   if termekek[i].ar > termekek[legdragabb_index].ar:
    legdragabb_index = i

  print(f"A termékek összértéke: {osszertek} Ft.")
  print(f"{ossz_200ft} db terméket lehet megvásárolni legfeljebb 200 Ft-ból.")
  print(f"A legdrágább termék neve: {termekek[legdragabb_index].nev}.")
  termek_keres = input("Add meg egy termék nevét! : ").strip().lower()

  talalat = keres(termek_keres)
  if talalat == -1:
   print("Nincs ilyen nevű termék :(")
  else:
   print(termekek[talalat])






