# @241105-2-2003
# feladat10.py
"""
10. Kérjük be a felhasználó tömegét kg-ban és magasságát cm-ben, majd számítsuk ki és írjuk a képernyőre a 
felhasználó testtömegindexét az alábbi képlet alapján!
TTI=𝒕ö𝒎𝒆𝒈/𝒎𝒂𝒈𝒂𝒔𝒔á𝒈^𝟐
Figyelj rá, hogy a képletben a magasság méterben megadott értékével kell számolni!
(testtomegindex)
"""

# Program run command in Android:Termux:Python :
runCmd = "python /storage/emulated/0/BitMiller/Pradhana/Dropbox/bitmiller_hu/verebely_progs/programozasi_alapok/gyakorlo_feladatok/feladatok1_pdf/feladat10.py"

# > https://hu.wikipedia.org/wiki/Testtömegindex

suly = float(input("Hány a kila, tesa? : "))
magassag = float(input("Osz', mennyire gór a centi? : "))/100
testtomegindex = round(suly/magassag**2, 3)

# idx = index
# dia = diagnozis
class Hatar:
 def __init__(self, idx, dia):
  self.idx = idx
  self.dia = dia

hatarok = [
 Hatar(0, "súlyosan sovány"),
 Hatar(16, "mérsékelten sovány"),
 Hatar(17, "enyhén sovány"),
 Hatar(18.5, "normális"),
 Hatar(25, "túlsúlyos"),
 Hatar(30, "I. fokúan elhízott"),
 Hatar(35, "II. fokúan elhízott"),
 Hatar(40, "III. fokúan elhízott"),
]

def kategoria(testtomegindex):
 global hatarok
 diagnozis = ""
 for i in hatarok:
  if testtomegindex < i.idx:
   break
  diagnozis = i.dia
 return diagnozis

diagnozis = kategoria(testtomegindex)

print(f"Itt a te testednek a tömegindexe: {testtomegindex} kg/m^2")
print(f"Na most az a helyzet, hogy a diagnózis (Dr. Wikipédia szerint): {diagnozis}")


