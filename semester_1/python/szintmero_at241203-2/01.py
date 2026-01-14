# @241203-2-1839
# Program run command in Android:Termux:Python :
runCmd = "python /storage/emulated/0/BitMiller/Pradhana/Dropbox/bitmiller_hu/verebely_progs/programozasi_alapok/szintmero_at241203-2/01.py"


def int_inp(s = ""):
 if s!="":
  print(s, end=" : ")
 while True:
  i1 = input()
  try:
   i2 = int(i1)
  except ValueError:
   print("Int-et adj! : ")
  else:
   break
 return i2

i = int_inp("Adj egy egész számot!")
print(i)

s = input("Most pedig egy tetszőleges karakterláncot (észszerű határok között) : ")

j = 0

for _ in range(i):
 print(s, end="")
 if j<i:
  print(" ", end="")
 j+=1