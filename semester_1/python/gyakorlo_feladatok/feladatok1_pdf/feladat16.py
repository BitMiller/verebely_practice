# @241106-3-2016
# feladat16.py
"""
Kérjük be a külső hőmérsékletet, és írassuk ki, ha fagy odakint! (fagy)
"""

# Program run command in Android:Termux:Python :
runCmd = "python /storage/emulated/0/BitMiller/Pradhana/Dropbox/bitmiller_hu/verebely_progs/programozasi_alapok/gyakorlo_feladatok/feladatok1_pdf/feladat16.py"


def float_input(s = "") :
 if s!="":
  print(s+" : ")
 while True:
  i1 = input()
  try:
   i2 = float(i1)
  except ValueError:
   print("Valami nórmálisat írjá má!")
  else: return i2


kulso_homerseklet = float_input("Mennyi kint a mérséklete a hőnek?")

if kulso_homerseklet<0:
 print("Cydry van odakü'!")
else:
 print("Végülis, nem olyan vészes. Pakolj fürdőgatyát!")

