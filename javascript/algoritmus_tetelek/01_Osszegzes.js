/*
Összegzés (X[N], S)
    S = 0;
    Ciklus i = 1-től N-ig
        S = S + X[i];
    Ciklus vége;
Eljárás vége;
*/

var szamok = new Array(12, 43, 87, -3);
var osszeg = 0;

function osszegzes (tomb, ossz) {
    ossz = 0;

    for (let i = 0; i < tomb.length; i++) {
        ossz = ossz + tomb[i];
    }

    return ossz;
}

console.log("A(z) [" + szamok + "] tömb elemeinek összege: " + osszegzes(szamok, osszeg));
