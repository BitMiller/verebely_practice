# @241106-3-2016
# feladat27.py
"""
Kérjük be egy nap sorszámát (1..7) numerikus formában, és írjuk ki a nap megnevezését a képernyőre
(hétfő, kedd, ..., vasárnap). Amennyiben a beírt sorszám nem 1..7 közötti szám, úgy a hibás adat kiírás jelenjen meg.
(hetnapjai)
"""

# Program run command in Android:Termux:Python :
runCmd = "python /storage/emulated/0/BitMiller/Pradhana/Dropbox/bitmiller_hu/verebely_progs/programozasi_alapok/gyakorlo_feladatok/feladatok1_pdf/feladat27.py"


class Napocska:
 def __init__(self, nap_szam, nap_nev):
  self.szam = nap_szam
  self.nev = nap_nev


napok = [
Napocska(1, "hétfő"),
Napocska(2, "kedd"),
Napocska(3, "szerda"),
Napocska(4, "csütörtök"),
Napocska(5, "péntek"),
Napocska(6, "szombat"),
Napocska(7, "vasárnap"),
]

print("Kérlek, valami napsorszámot adj már meg!\nSúgó:")
for i in napok:
 print(f"{i.szam} = {i.nev}")

nap_be = input("Nos? > ")

hiba = False

try:
 nap_be = float(nap_be)
except ValueError:
 hiba = True

if hiba:
 print("Hibás adat! Valami rejtélyes dolog félrement rejtélyesen.")
elif nap_be%1!=0:
 print("Az input numerikus, de nem egész szám, márpedig nekünk (legalábbis nekem) az kell! Lehet, hogy eddig erről nem szóltam, de szevasz.")
elif not (nap_be>0 and nap_be<8):
 print(f"Minden nagyon szép, de a(z) {nap_be} szám valamiért mégsem lesz jó! Lásd, kivel csevegsz: tőlem még végtelenszer próbálkozhatsz. De csak egy újabb programfuttatáskor :P")
else:
 print(f"A fáma a {napok[int(nap_be-1)].nev}-ról/-ről szól.")

