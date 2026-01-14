# @241119-2-1655
# feladat02.pdf

"""
Töltsünk fel egy 20 elemű tömböt 50 és 150 közötti véletlen számokkal, rendezzük a tömböt és írjuk ki az elemeit a képernyőre! Határozzuk meg az összegüket, átlagukat, valamint a 0-ra végződők számát!
"""


# Program run command in Android:Termux:Python :
runCmd = "python /storage/emulated/0/BitMiller/Pradhana/Dropbox/bitmiller_hu/verebely_progs/programozasi_alapok/gyakorlo_feladatok/feladatok3_pdf/feladat02.py"


from random import randint

numbers:list[int] = []

def in_list(n:int, l:list) :
 n_in = False
 for i in l :
  if i==n:
   n_in=True
   break
 return n_in

def generate_unique() :
 nums:list[int] = []
 for i in range(20) :
  while True:
   new_n = randint(50, 150)
   if not in_list(new_n, nums) :
    nums.append(new_n)
    break
 return nums

def generate_plain() :
 nums:list[int] = []
 for i in range(20) :
  nums.append(randint(50, 150))
 return nums

#numbers = generate_plain()
numbers = generate_unique()

print(f"A számok keletkezési sorrendjükben: {numbers}")

for i in range(len(numbers)-1) :
 for j in range(i+1, len(numbers)) :
  if numbers[i]>numbers[j] :
   tmp = numbers[i]
   numbers[i] = numbers[j]
   numbers[j] = tmp

print(f"A számok rendezve: {numbers}")

#befejezni