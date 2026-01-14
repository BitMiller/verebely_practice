# @241105-2-1905
# feladatok1.pdf
"""
1. Programunk kérje be egy ember lakhelyének irányítószámát, a várost, a közterület nevét, a közterület 
jellegét, a házszámot és végül írja ki egy sorban a következő formátumban:
Pl.: 1042 Budapest Tanoda tér 2. (lakcim)
"""

# Program run command in Android:Termux:Python :
runCmd = "python /storage/emulated/0/BitMiller/Pradhana/Dropbox/bitmiller_hu/verebely_progs/programozasi_alapok/gyakorlo_feladatok/feladatok1_pdf/feladat01.py"

# lakcím bekérése:

print("Add meg a következő adatokat:")
irsz = input("irányítószám: ")
varos = input("település: ")
kt_nev = input("közterület neve: ")
kt_jelleg = input("közterület jellege: ")
hsz = input("házszám: ")

print(irsz + " " + varos + " " + kt_nev + " " + kt_jelleg + " " + hsz)
print(f"{irsz} {varos} {kt_nev} {kt_jelleg} {hsz}")
print(irsz, varos, kt_nev, kt_jelleg, hsz, sep= " ")


