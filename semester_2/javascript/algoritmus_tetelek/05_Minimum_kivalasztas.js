/*
Minimum_kiválasztás(X[N], min)
    min = 1;
    Ciklus i = 2-től N-ig
        Ha X[i] < X[min], akkor
            min = i;
        Elágazás vége;
    Ciklus vége;
Eljárás vége;
*/

var szamok = new Array(6, -5, 14, 18);
var min_index;

function minimum_kivalasztas(x, min) {
    min = 0;

    for (let i = 0; i < x.length; i++) {
        if (x[i] < x[min]) {
            min = i;
        }
    }

    return min;
}

console.log("A(z) [" + szamok + "] tömb legkisebb eleme: " + szamok[minimum_kivalasztas(szamok, min_index)] + ", indexe: " + minimum_kivalasztas(szamok, min_index));
