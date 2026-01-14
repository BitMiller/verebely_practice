

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

