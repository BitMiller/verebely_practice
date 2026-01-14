

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
