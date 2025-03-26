
import os, random

MAX_ERRORS = 11

def cls():
 os.system("cls" if os.name=="nt" else "clear")

os.chdir(os.path.dirname(__file__))

with open("data.txt", "r", encoding="UTF-8") as f:
 data = f.readlines()

for i in range(len(data)):
 data[i] = data[i].strip().lower()

solution = data[random.randrange(len(data))]
riddle:list = ["_"] * len(solution)
game_exit = False
game_lost = False
game_won = False
guesses:list = []
errors:float = 0

while not (game_exit or game_lost or game_won):

 cls()
 print("Akasztófás játék v0.0015")
 print("Gondoltam egy szóra. Így néz ki:")
 print(f"{solution} (DEBUG: solution)")
 print("".join(riddle))
 print(f"Eddigi tippek: {guesses}")
 print(f"Össz hibapont lehet: {MAX_ERRORS}")
 print(f"Eddigi hibapontok: {errors}")
 print(f"Ennyi hibázási lehetőség az akasztásig: {(MAX_ERRORS-errors):.1f}")
 guess = input("Kérek egy betűt (kilépés: [Enter])! : ").lower()
 if guess == "":
  game_exit = True
 else:
  if guess not in guesses:
   guesses.append(guess)
   if guess in solution:
    for i in range(len(solution)):
     if solution[i] == guess:
      riddle[i] = guess
    if "_" not in riddle:
     game_won = True
   else:
    errors += 1
  else:
   print("Huppla, ez a bötü má vót! Lásd, kivel van dolgod, felszámolok 0.1 hibapontot. Nyugtázáshoz nyomj [Enter]-t, általad választott erősséggel!", end="")
   errors += 0.1
   input()
 if errors >= MAX_ERRORS:
  game_lost = True


if game_exit:
 print("Ügyesen kiléptél!")
elif game_lost:
 print("Ügyesen veszítettél! (Durva, hogy egy szó ki nem találásáért akasztás jár... Ezt a játékot biztosan unatkozó hóhérok találták ki.)")
else:
 print("Ügyesen nyertél!")
