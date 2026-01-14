# @241106-3-2016
# feladat14.py
"""
Programunk kérje be egy eszköz másodpercekben mért üzemidejét!
Eredményként adja meg …nap …óra …másodperc formában az üzemidőt! (uzemido)
"""

# Program run command in Android:Termux:Python :
runCmd = "python /storage/emulated/0/BitMiller/Pradhana/Dropbox/bitmiller_hu/verebely_progs/programozasi_alapok/gyakorlo_feladatok/feladatok1_pdf/feladat14.py"

from math import *

def getinput(s = ""):
 if s!="":
  print(s, end=" : ")
 while True:
  st = input()
  try:
   i = int(st)
  except ValueError:
   print("Egész számot, léccy! : ", end="")
  else:
   break;
 return i


uzemido_mp = getinput("Add meg az üzemidőt másodpercben")

tab_meret = 24

masodperc = uzemido_mp%60
perc = uzemido_mp//60%60
ora = uzemido_mp//3600%24
nap = uzemido_mp//(3600*24)


print(f"Üzemidő")
print(f"{'másodpercben':<{tab_meret}} : {uzemido_mp}")
print(f"{'percben':<{tab_meret}} : {(uzemido_mp/60):.3f}")
print(f"{'órában':<{tab_meret}} : {uzemido_mp/3600:.3f}")
print(f"{'napban':<{tab_meret}} : {round(uzemido_mp/86400, 3):.3f}")

print(f"{'Üzemidő szépen felbontva':<{tab_meret}} : {nap} nap {ora} óra {perc} perc {masodperc} másodperc")




