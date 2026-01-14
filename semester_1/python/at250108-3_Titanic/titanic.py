
prg_ver = "@250108-3-0625"

#run: python /storage/emulated/0/BitMiller/Pradhana/Dropbox/bitmiller_hu/verebely_progs/programozasi_alapok/at250108-3_Titanic/titanic.py

#help: https://www.w3schools.com/python/default.asp

print("\n==******************==")
print("    PROGRAM BEGIN    ")
print(f"version {prg_ver}")
print("----------------------\n")

from os import *
from os import open as os_open
#import os
from os import getcwd as a1
from os import getcwd as a2

chdir(path.dirname(__file__))
print(getcwd())
print(a1())
print(a2())

"""
with open("titanic.txt", "r") as f:
 i=1
"""
"""
 data = f.readlines()
 print(data)
"""


"""
try:
 with open("titanic.txt", "r") as f:
  data = f.readlines()
  print(data)
except Exception as e:
 print(e);
"""


print("\n----------------------")
print("     PROGRAM END")
print("==******************==\n")
