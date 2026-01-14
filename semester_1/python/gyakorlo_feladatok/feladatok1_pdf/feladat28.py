# @241106-3-2016
# feladat28.py
"""
Kérjük be egy hónap sorszámát (1..12) numerikus formában, és írjuk ki a hónap megnevezését a képernyőre
(január, ..., december). Amennyiben a beírt sorszám nem 1..12 közötti szám, úgy a hibás adat kiírás jelenjen meg.
(honapok)
"""

# Program run command in Android:Termux:Python :
runCmd = "python /storage/emulated/0/BitMiller/Pradhana/Dropbox/bitmiller_hu/verebely_progs/programozasi_alapok/gyakorlo_feladatok/feladatok1_pdf/feladat28.py"


class Honapocska:
 def __init__(self, szam, nev):
  self.szam = szam
  self.nev = nev


honapok = [
Honapocska(1, "Január"),
Honapocska(2, "Február"),
Honapocska(3, "Március"),
Honapocska(4, "Április"),
Honapocska(5, "Május"),
Honapocska(6, "Június"),
Honapocska(7, "Július"),
Honapocska(8, ""),
Honapocska(9, ""),
Honapocska(10, ""),
Honapocska(11, ""),
Honapocska(12, ""),
]


