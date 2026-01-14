# @241203-2-1839
# Program run command in Android:Termux:Python :
runCmd = "python /storage/emulated/0/BitMiller/Pradhana/Dropbox/bitmiller_hu/verebely_progs/programozasi_alapok/szintmero_at241203-2/03.py"


from sys import exit as kill
from math import *

szamok:list = []

print("Kérek három lebegőpontos számot!")

for i in range(3):
 szamok.append(float(input(f"{i+1}. szám : ")))


if (szamok[0]+szamok[1]>szamok[2] and
    szamok[0]+szamok[2]>szamok[1] and
    szamok[1]+szamok[2]>szamok[0]):
 print("Létezhet háromszög ilyen oldalhosszokkal.")
else:
 print("Nem létezhet háromszög ilyen oldalhosszokkal.")
 kill()

szamok.sort()
nem = ""

atfogo = round(sqrt(szamok[0]*szamok[0]+szamok[1]*szamok[1]), 2)
if atfogo != szamok[2]:
 nem = "NEM "
print(f"Gratulálok, a háromszög {nem}derékszögű!")


nem = ""
egyenlooldalu = False
if not (
szamok[0]==szamok[1] or
szamok[0]==szamok[2] or
szamok[1]==szamok[2]
):
  nem = "NEM "
elif szamok[0]==szamok[1] and szamok[0]==szamok[2]:
 egyenlooldalu = True

print(f"Gratulálok, a háromszög {nem}egyenlőszárú!")
if egyenlooldalu:
 print("Sőt, egyenlőoldalú!")

kerulet = szamok[0]+szamok[1]+szamok[2]
print(f"A háromszög kerülete: {kerulet} cm")

# Hérón-képlet: https://matematikamodszertan.hu/haromszog-terulete-oldalakbol/
s = kerulet/2
terulet = sqrt(s*(s-szamok[0])*(s-szamok[1])*(s-szamok[2]))

print(f"A háromszög területe: {round(terulet, 3)} cm^2")
