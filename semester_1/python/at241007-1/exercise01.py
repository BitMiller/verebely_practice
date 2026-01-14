#BEGIN#

prg_ver = "@241007-1-1907"
prg_dsc = ""

#run: python /storage/emulated/0/BitMiller/Pradhana/Dropbox/bitmiller_hu/progs/python_for_termux/__practice/at241007-1_Programozasi_alapok/exercise01.py

#help: https://www.w3schools.com/python/default.asp

print()
print("==******************==")
print("    PROGRAM BEGIN    ")
print(f"Version: {prg_ver}")
print(f"Description: {prg_dsc}")
print("----------------------\n\n")

#----------------------------------------#


print("PRG BEGIN")

nev = input ("Mi a neved? : ")

valasz = input(f"Szeretsz programozni, {nev}? : ")

print (f"Szasz, {nev}!")

if valasz == "igen":
    print("Jó!")
else:
    print(f"Ejaj, {nev}")

szam = int(input("Hányszor írjam ki, hogy \"bánón\"? : ")) #az int() az input-ot számmá alakítja

for _ in range(szam):
    print("banán")


#----------------------------------------#

print("\n\n----------------------")
print("     PROGRAM END")
print("==******************==")
print()

#END#