
szam = int(input('Adj meg egy számot: '))
szoveg =str(input('Adj meg egy szöveget: '))
for x in range(szam**2):
    print(f'{str.lower(szoveg)}', end=' ')

print('\n')

print("padadicsom:  1199 Ft/Kg")
paradicsom = float(1199)
print("paprika:     1349 Ft/Kg")
paprika = float(1349)
print("vöröshagyma: 289 Ft/Kg")
voroshagyma = float(289)

fizetendo = float(0)

vasarlas = 'igen'
while vasarlas == 'igen':
    vasarlas = str(input('kíván valamit vásárolni? '))
    if vasarlas == 'igen':
        valaszto = input('melyik termékből? ')
        if valaszto == 'paradicsom':
            kosar = float(input(f'Hány Kg {valaszto}(o)t szeretne? '))
            fizetendo += kosar * paradicsom
        elif valaszto == 'paprika':
            kosar = float(input(f'Hány Kg {valaszto}(o)t szeretne? '))
            fizetendo += kosar * paprika
        elif valaszto == 'vöröshagyma':
            kosar = float(input(f'Hány Kg {valaszto}(o)t szeretne? '))
            fizetendo += kosar * voroshagyma
    elif vasarlas == 'nem':
        print('Köszönjük a vásárlást!')
        print(f'fizetendő összeg: {fizetendo:.0f}Ft')

a = float(input('add meg az [a] értékét: '))
b = float(input('add meg az [b] értékét: '))
c = float(input('add meg az [c] értékét: '))

s:float = (a+b+c)/2 #háromszög kerületének a fele
t:float = (s*(s-a)*(s-b)*(s-c))**0.5 #a háromszög területe
#létezhet háromszög ilyen oldalakkal
if a+b > c and a+c > b and b+c > a:
    print('létezhet háromszög ilyen oldalhosszakkal')
else:
    print('ilyen oldalhosszakkal nem létezhet háromszög!')
#ez a háromszög derékszögű
an = a*2
bn = b*2
cn = c*2
if an + bn == cn or an + cn == bn or bn + cn == an:
    print('ez a háromszög derégszögű')
#ez a háromszög IGEN/NEM egyenlő szárú
if a == b or b == c or c == a:
    print('ez a háromszög egyenlőszárú')
else:
    print('ez a háromszög NEM egyenlőszárú')

print(f'a háromszög kerülete: {s * 2} cm')
print(f'a háromszög területe: {t:.2f} cm^2')

print('adja meg a másodfokú egyenlet együtthatóit!')
print('[ax^2 + bx + c = 0]')
a = int(input('a = '))
b = int(input('b = '))
c = int(input('c = '))

#megoldóképletek:
d = b**2 - 4*a*c # diszkrimináns

x1 = (-b + (d**0.5)) / (2*a)
x2 = (-b - (d**0.5)) / (2*a)


if a == 0:
    print('az egyenlet nem másodfokú')
elif d < 0:
    print('az egyenletnek nincs valós megoldása')
elif d == 0:
    print('az egyenletnek csak egy valós megoldása van')
    #megoldás
else:
    print('az egyenletnek két valós megoldása van:')
    print(f'xˇ1 = {x1}')
    print(f'xˇ2 = {x2}')
