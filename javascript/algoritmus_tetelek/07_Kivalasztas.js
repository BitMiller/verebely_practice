/*
Kiválasztás(X[N], T, sorszám)
    i = 1;
    Ciklus amíg X[i] nem T tulajdonságú
        i = i + 1
    Ciklus vége;
    sorszám = i;
Eljárás vége;
*/

var szamok = new Array(6, 55, 7, -30);
var tulajdonsag = 2;
var index;

function kivalasztas(x, t, sorszam) {
    let i = 0;

    while (x[i] % t != 0) {
        i = i + 1;
    }

    sorszam = i;

    return sorszam;
}

console.log("A(z) [" + szamok + "] tömbben az első " + tulajdonsag + "-val/-vel osztható szám: " + szamok[kivalasztas(szamok, tulajdonsag, index)] + " indexe: " + kivalasztas(szamok, tulajdonsag, index));
