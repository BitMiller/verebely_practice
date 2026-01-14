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


suly = float(input("Hány a kila, tesa? : "))
magassag = float(input("Osz', mennyire gór a centi? : "))/100
testtomegindex = round(suly/magassag, 3)

class Hatar:
 def __init__(self, idx, dia):
  self.idx = idx
  self.dia = dia

hatarok = [
 Hatar(16, "súlyosan sovány"),
 Hatar(17, dia = "mérsékelten sovány"),
 Hatar(18.5, dia = "enyhén sovány"),
 Hatar(25, dia = "normális"),
 Hatar(30, dia = "túlsúlyos"),
 Hatar(35, dia = "I. fokúan elhízott"),
 Hatar(40, dia = "II. fokúan elhízott"),
]



print(f"Itt a te testednek a tömegindexe: {hatarok} kg/m^2")
print("Na most az a helyzet, hogy ", )


