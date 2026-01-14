# @241106-3-2016
# feladat20.py
"""
Olvasson be a billentyűzetről egy számot és mondjuk meg, hogy a szám negatív, vagy pozitív vagy egyik sem! (elojel)
"""

# Program run command in Android:Termux:Python :
runCmd = "python /storage/emulated/0/BitMiller/Pradhana/Dropbox/bitmiller_hu/verebely_progs/programozasi_alapok/gyakorlo_feladatok/feladatok1_pdf/feladat20.py"


def com_n_get_szam(s=""):
 if s!="": print(s+" : ", end="")
 while True:
  inp = input()
  try: res = float(inp)
  except ValueError: print("Elhiszem, hogy jót akartál, de próbáld meg még egyszer! : ")
  else: return res


szam = com_n_get_szam("Ha gondolod, jöhet egy szám!")
print(f"Ez a szám {'pozitív!' if szam>0 else 'negatív!' if szam<0 else 'egyik sem! B=Đ-- O:) (Emojic-Magic rulez!)'}")


