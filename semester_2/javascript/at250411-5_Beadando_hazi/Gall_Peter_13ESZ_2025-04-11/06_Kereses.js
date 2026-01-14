/*
Keresés(X[N], T, sorszám)
    i = 1;
    Ciklus amíg i <= N és X[i] nem T tulajdonságú
        i = i + 1;
    Ciklus vége;
    Ha i <= N akkor
        sorszám = i;
    Különben
        sorszám = -1;
    Elágazás vége;
Eljárás vége;
*/

var szamok = new Array(5, 8, 93, 2);
var tulajdonsag = 2;
var index;

function kereses(x, t, sorszam) {
    let i = 0;

    while (i < x.length && x[i] != t) {
        i = i + 1;
    }

    if (i < x.length) {
        sorszam = i;
    }

    else {
        sorszam = -1;
    }

    return sorszam;
}

console.log("A(z) [" + szamok + "] tömbben a(z) " + tulajdonsag + " szám (első előfordulási helyének) indexe (ha nincs, akkor -1) : " + kereses(szamok, tulajdonsag, index));
