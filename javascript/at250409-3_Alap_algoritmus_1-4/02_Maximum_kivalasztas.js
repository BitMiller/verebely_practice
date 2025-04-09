var szamok = new Array(6, -8, 7, 77);
var max;

function maximum_kivalasztas(tomb, m) {
    m = 0;

    for (let i = 1; i < tomb.length; i++) {
        if (tomb[i] > tomb [m]) {
            m = i;
        }
    }

    return m;
}

console.log("Maxadik elem: " + szamok[maximum_kivalasztas(szamok, max)] + ", indexe: " + maximum_kivalasztas(szamok, max));
