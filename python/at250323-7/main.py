import os

os.chdir(os.path.dirname(__file__))

#print(os.getcwd())

feladat = 3

#if True:
#    if True:

match feladat:
    case 1:
        print("1. feladat:")

    case 2:
        print("2. feladat:")


    case 3:
        print("3. feladat:")
        
        class Ember:
            def __init__(self, ln):
                ln = ln.strip().split(";")
                self.csaladnev = ln[0]
                self.keresztnev1 = ln[1]
                self.keresztnev2 = ln[2]
                self.jelzok = ln[3].strip().split(",")
                self.nem = ln[4]
                self.szuletes = [int(x) for x in ln[5].split("-")]
                self.munkakor = ln[6]
                self.fizetes = int(ln[7])
                
                tmp:list = []
                for i in range(len(self.jelzok)):
                    if self.jelzok[i] != "":
                        tmp.append(self.jelzok[i])
                self.jelzok = list(tmp)
                
            def __repr__(self):
                s:str = f"Családnév: {self.csaladnev}, Keresztnév: {self.keresztnev1}, "
                if self.keresztnev2 != "":
                    s += f"2. keresztnév: {self.keresztnev2}, "
                for i in range(len(self.jelzok)):
                    s += f"{i+1}. név előtét: {self.jelzok[i]}, "
                s += f"Nem: {self.nem}, Születési dátum: {self.szuletes[0]}.{self.szuletes[1]}.{self.szuletes[2]}., Munkakör: {self.munkakor}, Fizetés: {self.fizetes}"
                
                return s
        
        with open("random_people.csv", "r", encoding="UTF-8") as f:
            data = f.readlines()

        #print(data)
        
        emberek:list[Ember] = []

        for i in range(1, len(data)):
            emberek.append(Ember(data[i]))
            
        print(emberek)
            
# Hány ember van
# Ffiak és nők aránya
# Hány féle név előtét van
# Hány féle keresztnév van
# Kinek nincs második keresztneve (teljes névvel)
# Ki keres 300.000 Ft alatt
# Ffi és női átlagfizu aránya
# Van-e azonos napon született (év nem számít)
# Átlag születési dátum
# A szökőévben születettek családnevében található mássalhangzó fajták számának és a többi ember fizetésében található számjegyek összege aránya reciprokának értéke, nyolc tizedesjegy pontossággal
