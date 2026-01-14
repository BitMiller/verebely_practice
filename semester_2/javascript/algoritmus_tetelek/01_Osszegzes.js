/*
Összegzés (X[N], S)
    S = 0;
    Ciklus i = 1-től N-ig
        S = S + X[i];
    Ciklus vége;
Eljárás vége;
*/

var szamok = new Array(12, 43, 87, -3);
var szum;

function osszegzes (x, s) {
    s = 0;

    for (let i = 0; i < x.length; i++) {
        s = s + x[i];
    }

    return s;
}

console.log("A(z) [" + szamok + "] tömb elemeinek összege: " + osszegzes(szamok, szum));
