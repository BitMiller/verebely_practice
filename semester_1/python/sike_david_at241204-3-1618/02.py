


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

        