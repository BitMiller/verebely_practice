# @241105-2-1751


print("Mi a te neved, kincsem? : ")
nev = input()
print(f"Aha, {nev}")
print(f"És oszt mennyi az idő mostanába', {nev}? (elfogadott formátum: óra:perc) : ")
ido = input()

ido = ido.split(":")

ido_float = [float(x) for x in ido]
for x in ido_float:
 print(x)

time_of_day = ido[0]+ido[1]*(1/60)

print(f"Akkor most tulajdonképpen {float(time_of_day)} óra van!")



