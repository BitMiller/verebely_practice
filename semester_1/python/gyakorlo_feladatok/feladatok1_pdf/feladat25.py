# @241106-3-2016
# feladat25.py
"""
A program kérjen be két számot, és egy műveleti jelet (+,-,/,*), majd írja ki a művelet eredményét. (muvelet)
"""

# Program run command in Android:Termux:Python :
runCmd = "python /storage/emulated/0/BitMiller/Pradhana/Dropbox/bitmiller_hu/verebely_progs/programozasi_alapok/gyakorlo_feladatok/feladatok1_pdf/feladat25.py"

keplet = input("Írgyá vmi varázslatot : ")

print(f"Illyen eredményes a müvellett: {str(eval(keplet)).rstrip('0').rstrip('.')}")

"""
szam1 = float(input("Szám 1 : "))
muvelet = input("Műveleti jel : ")
szam2 = float(input("Szám 2 : "))

print("A müvellett eredményessége: ", end="")

match muvelet:
 case "+": print(str(szam1+szam2).rstrip("0").rstrip("."))
 case "-": print(str(szam1-szam2).rstrip("0").rstrip("."))
 case "*": print(str(szam1*szam2).rstrip("0").rstrip("."))
 case "/": print(str(szam1/szam2).rstrip("0").rstrip("."))
 case _: print("Hááát, énnemist'om micsinájak.")
"""

