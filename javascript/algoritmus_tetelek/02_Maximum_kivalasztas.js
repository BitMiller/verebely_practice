/*
Maximum_kiválasztás (X[N], max)
    max = 1;
    Ciklus i=2-től N-ig
        Ha X[i] > X[max], akkor
            max = i;
        Elágazás vége;
    Ciklus vége;
Eljárás vége;
*/

var szamok = new Array(12, 43, 87, -3);
var max_index = 0;

function maximum_kivalasztas(tomb, max) {
    let max = 0;

    for (let i = 1; i < tomb.length; i++) {
        if (tomb[i] > tomb[max]) {
            max = i;
        }
    }

    return max;
}

console.log("A(z) [" + szamok + "] tömb legnagyobb eleme: " + szamok[maximum_kivalasztas(szamok, max_index)] + ", indexe: " + maximum_kivalasztas(szamok, max_index));
