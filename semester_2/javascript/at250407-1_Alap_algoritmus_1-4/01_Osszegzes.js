/*
Összegzés (X[N], S)
    S = 0;
    Ciklus i = 1-től N-ig
        S = S + X[i];
    Ciklus vége;
Eljárás vége;
*/

var szamok = new Array(13, -4, 50, 2);
var szum = 0;

function osszegzes(x, s) {
    s = 0;

    for (let i = 0; i < x.length; i++) {
        s = s + x[i];
    }

    return s;
}

console.log(osszegzes(szamok, szum));