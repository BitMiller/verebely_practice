# @241203-2-1839
# Program run command in Android:Termux:Python :
runCmd = "python /storage/emulated/0/BitMiller/Pradhana/Dropbox/bitmiller_hu/verebely_progs/programozasi_alapok/szintmero_at241203-2/04.py"


from math import *

def float_input(s=""):
 if s!="": print(s, end=" : ")
 while True:
  f1 = input()
  try: f2 = float(f1)
  except ValueError: print("Na azért légyszi már! Mi ez? Lebegjen az a szám pontosan! : ", end="")
  else: break
 return f2

a = float_input("Kérem 'a'-t")
b = float_input("Kérem 'b'-t")
c = float_input("Kérem 'c'-t")

if a==0:
 print("'a' nem lehet nulla, szevasz! Legközelebb majd jobban vigyázol.")
else:
 diszkriminans = b*b-4*a*c
 if diszkriminans<0:
  print("Az egyenletnek nincs megoldása a valós számok halmazán!")
 else:
  megoldas1 = (-b+sqrt(diszkriminans))/(2*a)
  megoldas2 = (-b-sqrt(diszkriminans))/(2*a)

  if diszkriminans==0:
   print(f"Az egyenletnek egy valós megoldása van: {round(megoldas1, 2)}")
  else:
   print(f"Az egyenlet megoldásai a valós számok halmazán: {round(megoldas1, 2)} , {round(megoldas2, 2)}")

