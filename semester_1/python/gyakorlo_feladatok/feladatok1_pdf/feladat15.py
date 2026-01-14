# @241106-3-2016
# feladat15.py
"""
Írjunk programot, amely kiszámítja egy autóval megtett útra fizetett költségtérítést!
A program kérje be a megtett út hosszát km-ben, az autó fogyasztását 100 km-en literben valamint az üzemanyag árát
és ezek ismeretében számítsa ki az üzemanyagköltséget. A megtett útra, a fogyasztásra ,
és az üzemanyag árára is fogadjon el tört számokat is.
[Az üzemanyagköltség kiszámítására használd az alábbi képletet:
üzemanyagköltség=(út*fogyasztás*üzemanyag ár)/100 ]
A költségtérítés összege 100 km-nél nem hosszabb út esetén maga az üzemanyagköltség,
ennél hosszabb út esetén az üzemanyagköltséghez hozzáadják a megtett út 25-szörösét és így kapjuk meg a költségtérítést.
A program címe "Utazási költségtérítés" legyen és minta szerinti formában írja ki az adatokat! (utazasikoltseg)
[...] -> pdf
"""

# Program run command in Android:Termux:Python :
runCmd = "python /storage/emulated/0/BitMiller/Pradhana/Dropbox/bitmiller_hu/verebely_progs/programozasi_alapok/gyakorlo_feladatok/feladatok1_pdf/feladat15.py"


megtett = float(input("Megtett út hosszi? : "))
szazon = float(input("Hogy zabál százon? : "))
benya = float(input("Mennya benya? : "))

ktg:float = 0
ktg=float(megtett*szazon/100*benya)

#print(f"{ktg:=float(megtett*szazon/100*benya)}")
print(f"Kőcség : {ktg}")

if megtett<=100:
 print(f"A ktgtérítés az üzemanyagktg összege, azaz {ktg} Ft.")
else:
 print(f"Nagyon kis rendes vagy, 100km felett kavirnyálsz! Jutalmul ennyi a ktgtérítésed: {ktg+megtett*25}")


