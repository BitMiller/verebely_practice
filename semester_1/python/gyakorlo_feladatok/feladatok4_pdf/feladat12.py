# @241119-2-1655
# feladat12.pdf

"""
Döntsük el, hogy van-e egy szóban "ly" betű !
"""

# Program run command in Android:Termux:Python :
runCmd = "python /storage/emulated/0/BitMiller/Pradhana/Dropbox/bitmiller_hu/verebely_progs/programozasi_alapok/gyakorlo_feladatok/feladatok4_pdf/feladat12.py"

inp = input("AdLY egy szót! : ")


"""
van:bool = False

for i in range(len(inp)-1):
 if inp[i:2].lower()=="ly":
  van = True
  break

if van:
 print("Van LY!")
else: print("Nüncs LY.")
"""

if "ly" in inp.lower():
 print("Van!")
else: print("Nüncs.")

