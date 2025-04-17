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
var tulajdonsag = 6;
var index;

function kivalasztas(x, t, sorszam) {
    let i = 0;

    while (x[i] != t) {
        i = i + 1;
    }

    sorszam = i;

    return sorszam;
}

console.log("A(z) [" + szamok + "] tömbben a(z) " + tulajdonsag + " szám (első előfordulási helyének) indexe: " + kivalasztas(szamok, tulajdonsag, index));
