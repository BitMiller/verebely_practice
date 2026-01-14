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

//var szamok = new Array(5, 8, 93, 2);
var szamok = new Array(5, 7, 93, 1);
var tulajdonsag = 2;
var index;

function kereses(x, t, sorszam) {
    let i = 0;

    while (i < x.length && x[i] % t != 0) {
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

console.log("A(z) [" + szamok + "] tömbben az első " + tulajdonsag + "-val/-vel osztható szám indexe: " + kereses(szamok, tulajdonsag, index));
